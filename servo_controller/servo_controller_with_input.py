"""
David Anapolsky
Request a Charger
Servo Controller
"""

"""

Command format: servoIndex.position
Valid positions: 0 for unlocked, 1 for locked

# Servo Values:
Max = Unlocked = 0
Min = Locked = 1

Wiring:
Signal   -> Yellow -> White -> Signal
Positive -> Red    -> Red   -> Positive
Negative -> Brown  -> Black -> Negative
"""

# From the servo module import the classes and constants to control the servos
from servo import Servo, Calibration, servo2040, ANGULAR

# Import sleep to wait for the servo to move before disabling
from time import sleep

def main():
    
    # Create a custom calibration that matches the servo specifications
    cal = Calibration(ANGULAR)
    
    # Set the range to 200 degrees for the servos we are using
    WIDE_ANGLE_RANGE = 200

    # Modify the calibration to increase its range
    cal.first_value(-WIDE_ANGLE_RANGE / 2)
    cal.last_value(WIDE_ANGLE_RANGE / 2)

    # Create a list of the 12 servos with the custom calibration
    START_PIN = servo2040.SERVO_1
    END_PIN = servo2040.SERVO_12
    servos = [Servo(pin, cal) for pin in range(START_PIN, END_PIN + 1)]
    numServos = len(servos)

    # Start all the servos at their min positions, or locked
    for s in servos:
        s.to_min()
        #s.to_max() # Uncomment to open all lockers
    # Sleep for 2 seconds
    sleep(2)
    
    # Disable all the servos to increase their lifespan
    for s in servos:
        s.disable()

    # Try for testing purposes
    try:
        # Forever
        while True:

            # Get input
            command = input('Command: ')

            # Parse the command
            servoIndex, position = command_parse(command, numServos)

            # If the command was valid
            if servoIndex != 'Invalid':

                # If the position is 1, go to the min to close the locker
                if position == 1:
                    servos[servoIndex].to_min()
                    print('Output: Servo', servoIndex, 'is closed')
                    
                    # Sleep for 2 seconds
                    sleep(2)

                    # Disable again to increase its lifespan
                    servos[servoIndex].disable()

                # Else, if position is 0, go to the max to open the locker
                else:
                    servos[servoIndex].to_max()
                    print('Output: Servo', servoIndex, 'is open')

            # Else, print the command was invalid
            else: print('Output: Invalid command')

    except KeyboardInterrupt:
        print('Cleaning up')
        for s in servos:
            s.disable()

def command_parse(command, numServos):
    """
    Command format: servoIndex.position
    Valid positions: 0 for unlocked, 1 for locked
    """
    # Create a valid flag to determine if the command is valid
    VALID = False

    try:
        # Get the servo and position
        servo, position = map(int, command.split('.'))
        print(servo,position)

    # Catch a ValueError
    except ValueError:
        pass

    # Else, if the servo number is valid and the position is valid, set the valid flag to True
    else:
        if servo >= 0 and servo < numServos and position in (0,1):
            VALID = True

    finally:
        # If the input was valid, return the servo and position
        if VALID:
            return servo, position

        # Else, if something was invalid, return Invalid 
        else:
            return 'Invalid', 'Invalid'

main()
