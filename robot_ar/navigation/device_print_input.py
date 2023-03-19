#!/usr/bin/env python3

import inputs

devices = inputs.devices.gamepads
print(f"Connected devices: {devices}")

gamepad = inputs.devices.gamepads[0]

while True:
    events = gamepad.read()
    for event in events:
        print("Type of data code:" ,type(event.code), "         Type of state code: ", type(event.state))

