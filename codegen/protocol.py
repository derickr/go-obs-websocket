# RUN GOFMT BEFORE LOOKING AT THE OUTPUT PLEASE.

import json
import os
import sys
from typing import Dict, List, Tuple

package = "obsws"

type_map = {
    "bool": "bool",
    "boolean": "bool",
    "int": "int",
    "float": "float64",
    "double": "float64",
    "string": "string",
    "array": "[]string",
    "object": "map[string]interface{}",
    "array of objects": "[]map[string]interface{}",
    "scene": "interface{}",  # String?
    "object|array": "interface{}",
    "scene|array": "interface{}",
    "source|array": "interface{}",
}

unknown_types = [
    "object|array",
    "scene|array",
    "scene",  # String?
    "source|array",
]


def optional_type(s: str) -> Tuple[str, bool]:
    if s.endswith("(optional)"):
        return s[:s.find("(optional)")].strip(), True
    return s, False


def process_json(d: Dict):
    gen_events(d["events"])
    gen_requests(d["requests"])


def gen_events(events: Dict):
    """Generate all events."""
    for category, data in events.items():
        gen_events_category(category, data)


def gen_events_category(category: str, data: Dict):
    """Generate all events in one category."""
    events = "\n\n".join(gen_event(event) for event in data)
    with open(go_filename("events", category), "w") as f:
        f.write(f"""\
        package {package}

        // This file is automatically generated.
        // https://github.com/christopher-dG/go-obs-websocket/blob/master/codegen/protocol.py

        {events}
        """)


def gen_event(data: Dict) -> str:
    """Write Go code with a type definition and interface functions."""
    reserved = ["Type", "StreamTC", "RecTC"]
    if data.get("returns"):
        struct = f"""\
        type {data['name']}Event struct {{
            {go_variables(data['returns'], reserved)}
            _event
        }}\
        """
    else:
        struct = f"type {data['name']}Event _event"

    description = data["description"].replace("\n", " ")
    description = f"{data['name']}Event : {description}"
    if description and not description.endswith("."):
        description += "."
    if data.get("since"):
        description += f" Since: {data['since'].capitalize()}."

    return f"""\
    // {description}
    // https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#{data['heading']['text'].lower()}
    {struct}

    // Type returns the event's update type.
    func (e {data['name']}Event) Type() string {{ return e.UpdateType }}

    // StreamTC returns the event's stream timecode.
    func (e {data['name']}Event) StreamTC() string {{ return e.StreamTimecode }}

    // RecTC returns the event's recording timecode.
    func (e {data['name']}Event) RecTC() string {{ return e.RecTimecode }}
    """


def gen_requests(requests: Dict):
    """Generate all requests and responses."""
    for category, data in requests.items():
        gen_requests_category(category, data)


def gen_requests_category(category: str, data: Dict):
    requests = "\n\n".join(gen_request(request) for request in data)
    with open(go_filename("requests", category), "w") as f:
        f.write(f"""\
        package {package}

        // This file is automatically generated.
        // https://github.com/christopher-dG/go-obs-websocket/blob/master/codegen/protocol.py

        {requests}
        """)


def gen_request(data: Dict) -> str:
    """Write Go code with type definitions and interface functions."""
    reserved = ["ID", "Type"]
    if data.get("params"):
        struct = f"""\
        type {data['name']}Request struct {{
            {go_variables(data['params'], reserved)}
            _request
        }}
        """
    else:
        struct = f"type {data['name']}Request _request"

    description = data["description"].replace("\n", " ")
    description = f"{data['name']}Request : {description}"
    if description and not description.endswith("."):
        description += "."
    if data.get("since"):
        description += f" Since: {data['since'].capitalize()}."

    request = f"""\
    // {description}
    // https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#{data['heading']['text'].lower()}
    {struct}

    // ID returns the request's message ID.
    func (r {data['name']}Request) ID() string {{ return r.MessageID }}

    // Type returns the request's message type.
    func (r {data['name']}Request) Type() string {{ return r.RequestType }}
    """

    if data.get("returns"):
        reserved = ["ID", "Stat", "Err"]
        struct = f"""\
        type {data['name']}Response struct {{
            {go_variables(data['returns'], reserved)}
            _response
        }}
        """
    else:
        struct = f"type {data['name']}Response _response"

    description = f"{data['name']}Response : Response for {data['name']}Request."
    if data.get("since"):
        description += f" Since: {data['since'].capitalize()}."

    response = f"""\
    // {description}
    // https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#{data['heading']['text'].lower()}
    {struct}

    // ID returns the response's message ID.
    func (r {data['name']}Response) ID() string {{ return r.MessageID }}

    // Stat returns the response's status.
    func (r {data['name']}Response) Stat() string {{ return r.Status }}

    // Err returns the response's error.
    func (r {data['name']}Response) Err() string {{ return r.Error }}
    """

    return f"{request}\n\n{response}"


def go_variables(names: List, reserved: List) -> str:
    """
    Convert a list of variable names into Go code to be put
    inside a struct definition.
    """
    lines, varnames = [], []
    for v in names:
        typename, optional = optional_type(v["type"])
        varname = go_var(v["name"])
        description = v["description"].replace("\n", " ")
        if description and not description.endswith("."):
            description += "."
        tag = '`json:"%s"`' % v['name']
        line = f"{go_var(v['name'])} {type_map[typename.lower()]} {tag} // {description}"
        if optional:
            line += " Optional." if description else "Optional."
        if varname in reserved:
            line += " TODO: Reserved name."
        if varname in varnames:
            line += " TODO: Duplicate name."
        else:
            varnames.append(varname)
        if typename.lower() in unknown_types:
            line += f" TODO: Unknown type ({v['type']})."
        lines.append(line)
    return "\n".join(lines)


def go_var(s: str) -> str:
    """Convert a variable name in the input file to a Go variable name."""
    s = f"{s[0].upper()}{s[1:]}"
    for sep in ["-", "_", ".*.", "[].", "."]:
        while sep in s:
            _len = len(sep)
            if s.endswith(sep):
                s = s[:-_len]
                continue
            i = s.find(sep)
            s = f"{s[:i]}{s[i+_len].upper()}{s[i+_len+1:]}"

    return s.replace("Id", "ID")  # Yuck.


def go_filename(category, section):
    """Generate a Go filename from a category and section."""
    return f"{category}_{section.replace(' ', '_')}.go"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing filename argument")
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"file '{sys.argv[1]}' does not exist")
        exit(1)

    with open(sys.argv[1]) as f:
        d = json.load(f)

    process_json(d)
