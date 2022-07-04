"""
Test for the User Button
"""
from pimoroni import Button
from servo import servo2040

#Button(button, invert=True, repeat_time=200, hold_time=1000)

user_sw = Button(servo2040.USER_SW)

while True:
    if user_sw.read():
        print('Hello World')
