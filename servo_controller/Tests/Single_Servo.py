import time
import math
from servo import Servo, servo2040, ANGULAR

"""
Demonstrates how to create a Servo object and control it.
"""

# -----------------------------------------------------
# Create and modify the calibration of an angular servo
# -----------------------------------------------------

# Create an angular servo on pin 0. By default its value ranges from -90 to +90
s = Servo(servo2040.SERVO_1, ANGULAR)

# Access its calibration and print it out
cal = s.calibration()
print("Angular Servo:", cal, end="\n\n")


WIDE_ANGLE_RANGE = 200  # The range we want the anglular servo to cover # 200 degrees for servos we are using

# Lets modify the calibration to increase its range
cal.first_value(-WIDE_ANGLE_RANGE / 2)
cal.last_value(WIDE_ANGLE_RANGE / 2)

# Now apply the modified calibration to the servo and confirm it worked
s.calibration(cal)
print("Wide Angle Servo:", s.calibration(), end="\n\n")

def main():

    # Enable the servo (this puts it at the middle)
    s.enable()
    time.sleep(5)

    # Go to min
    s.to_min()
    time.sleep(2)

    # Go to max
    s.to_max()
    time.sleep(2)

    # Go back to mid
    s.to_mid()
    time.sleep(2)


    SWEEPS = 3              # How many sweeps of the servo to perform
    STEPS = 10              # The number of discrete sweep steps
    STEPS_INTERVAL = 0.5    # The time in seconds between each step of the sequence
    SWEEP_EXTENT = 90.0     # How far from zero to move the servo when sweeping

    # Do a sine sweep
    for j in range(SWEEPS):
        for i in range(360):
            s.value(math.sin(math.radians(i)) * SWEEP_EXTENT)
            time.sleep(0.02)

    # Do a stepped sweep
    for j in range(SWEEPS):
        for i in range(0, STEPS):
            s.to_percent(i, 0, STEPS, 0.0 - SWEEP_EXTENT, SWEEP_EXTENT)
            time.sleep(STEPS_INTERVAL)

    for i in range(0, STEPS):
        s.to_percent(i, STEPS, 0, 0.0 - SWEEP_EXTENT, SWEEP_EXTENT)
        time.sleep(STEPS_INTERVAL)

    # Disable the servo
    s.disable()

try:
    main()
except KeyboardInterrupt:
    print('Cleaning up')
    s.disable()