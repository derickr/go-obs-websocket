package obsws

// This file is automatically generated.
// https://github.com/christopher-dG/go-obs-websocket/blob/master/codegen/protocol.py

// StartStopReplayBufferRequest : Toggle the Replay Buffer on/off. Since: 4.2.0.
// https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#startstopreplaybuffer
type StartStopReplayBufferRequest _request

// ID returns the request's message ID.
func (r StartStopReplayBufferRequest) ID() string { return r.MessageID }

// Type returns the request's message type.
func (r StartStopReplayBufferRequest) Type() string { return r.RequestType }

// StartStopReplayBufferResponse : Response for StartStopReplayBufferRequest. Since: 4.2.0.
// https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#startstopreplaybuffer
type StartStopReplayBufferResponse _response

// ID returns the response's message ID.
func (r StartStopReplayBufferResponse) ID() string { return r.MessageID }

// Stat returns the response's status.
func (r StartStopReplayBufferResponse) Stat() string { return r.Status }

// Err returns the response's error.
func (r StartStopReplayBufferResponse) Err() string { return r.Error }

// StartReplayBufferRequest : Start recording into the Replay Buffer. Will return an `error` if the Replay Buffer is already active or if the "Save Replay Buffer" hotkey is not set in OBS' settings. Setting this hotkey is mandatory, even when triggering saves only through obs-websocket. Since: 4.2.0.
// https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#startreplaybuffer
type StartReplayBufferRequest _request

// ID returns the request's message ID.
func (r StartReplayBufferRequest) ID() string { return r.MessageID }

// Type returns the request's message type.
func (r StartReplayBufferRequest) Type() string { return r.RequestType }

// StartReplayBufferResponse : Response for StartReplayBufferRequest. Since: 4.2.0.
// https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#startreplaybuffer
type StartReplayBufferResponse _response

// ID returns the response's message ID.
func (r StartReplayBufferResponse) ID() string { return r.MessageID }

// Stat returns the response's status.
func (r StartReplayBufferResponse) Stat() string { return r.Status }

// Err returns the response's error.
func (r StartReplayBufferResponse) Err() string { return r.Error }

// StopReplayBufferRequest : Stop recording into the Replay Buffer. Will return an `error` if the Replay Buffer is not active. Since: 4.2.0.
// https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#stopreplaybuffer
type StopReplayBufferRequest _request

// ID returns the request's message ID.
func (r StopReplayBufferRequest) ID() string { return r.MessageID }

// Type returns the request's message type.
func (r StopReplayBufferRequest) Type() string { return r.RequestType }

// StopReplayBufferResponse : Response for StopReplayBufferRequest. Since: 4.2.0.
// https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#stopreplaybuffer
type StopReplayBufferResponse _response

// ID returns the response's message ID.
func (r StopReplayBufferResponse) ID() string { return r.MessageID }

// Stat returns the response's status.
func (r StopReplayBufferResponse) Stat() string { return r.Status }

// Err returns the response's error.
func (r StopReplayBufferResponse) Err() string { return r.Error }

// SaveReplayBufferRequest : Flush and save the contents of the Replay Buffer to disk. This is basically the same as triggering the "Save Replay Buffer" hotkey. Will return an `error` if the Replay Buffer is not active. Since: 4.2.0.
// https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#savereplaybuffer
type SaveReplayBufferRequest _request

// ID returns the request's message ID.
func (r SaveReplayBufferRequest) ID() string { return r.MessageID }

// Type returns the request's message type.
func (r SaveReplayBufferRequest) Type() string { return r.RequestType }

// SaveReplayBufferResponse : Response for SaveReplayBufferRequest. Since: 4.2.0.
// https://github.com/Palakis/obs-websocket/blob/master/docs/generated/protocol.md#savereplaybuffer
type SaveReplayBufferResponse _response

// ID returns the response's message ID.
func (r SaveReplayBufferResponse) ID() string { return r.MessageID }

// Stat returns the response's status.
func (r SaveReplayBufferResponse) Stat() string { return r.Status }

// Err returns the response's error.
func (r SaveReplayBufferResponse) Err() string { return r.Error }
