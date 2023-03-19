#!/usr/bin/env python3

import inputs

devices = inputs.devices.gamepads
print(f"Connected devices: {devices}")

gamepad = inputs.devices.gamepads[0]

while True:
    events = gamepad.read()
    for event in events:
        print("This evtype: ",event.ev_type, "This ev_code:", event.code, "This ev_state:", event.state)

