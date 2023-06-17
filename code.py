# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Example for Pico. Blinks the built-in LED."""
import time
import board
import digitalio

led_1 = digitalio.DigitalInOut(board.GP13)
led_1.direction = digitalio.Direction.OUTPUT

led_2 = digitalio.DigitalInOut(board.GP12)
led_2.direction = digitalio.Direction.OUTPUT

led_3 = digitalio.DigitalInOut(board.GP11)
led_3.direction = digitalio.Direction.OUTPUT

while True:
    for counter1 in range(1):
        for counter2 in range(1):
            for counter3 in range(1):
                print(counter1 + ", " + counter2 + ", " + counter3)
                led_1.value = counter1
                led_2.value = counter2
                led_3.value = counter3
                time.sleep(0.5)
