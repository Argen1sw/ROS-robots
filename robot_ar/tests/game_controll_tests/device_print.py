#!/usr/bin/env python3

import pygame

pygame.init()

# Initialize the game controller
pygame.joystick.init()

# Check how many game controllers are connected
joystick_count = pygame.joystick.get_count()
print(f"Number of game controllers: {joystick_count}")

# Get the first game controller
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Print some information about the game controller
print(f"Name of game controller: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")

# Get the current state of the axes
axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
print(f"Current state of axes: {axes}")
