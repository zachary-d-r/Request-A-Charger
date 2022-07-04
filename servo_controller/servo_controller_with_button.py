"""
David Anapolsky
Request a Charger
Servo Controller with Button for Testing
"""

"""
Max = Locked
Min = Unlocked

Signal   -> Yellow -> White -> Signal
Positive -> Red    -> Red   -> Positive
Negative -> Brown  -> Black -> Negative
"""

# From the servo module import the classes and constants to control the servos
from servo import Servo, Calibration, servo2040, ANGULAR

# Import button for testing the positioning of the servos
from pimoroni import Button

def main():
    
    # Create a button for the boot button
    user_sw = Button(servo2040.USER_SW)
    
    # Create a custom calibration that matches the servo specifications
    cal = Calibration(ANGULAR)
    
    # Set the range to 200 degrees for the servos we are using
    MAX = 100
    MIN = -100

    # Lets modify the calibration to increase its range
    cal.first_value(MIN)
    cal.last_value(MAX)

    # Create a list of the 12 servos with the custom calibration
    START_PIN = servo2040.SERVO_1
    END_PIN = servo2040.SERVO_12
    servos = [Servo(pin, cal) for pin in range(START_PIN, END_PIN + 1)]

    # Start all the servos at their mid position
    for s in servos:
        s.to_mid()
    try:
        # Forever
        while True:

            # If the button is pressed
            if user_sw.read():
                
                # Get the current value
                value = servos[1].value()
                
                # If the value is the max, go to the min for all servos
                if value == MAX:
                    for s in servos:
                        s.to_min()
                    print('At Min')
                
                # Else if the value is min or mid, go to max for all servos
                else:
                    for s in servos:
                        s.to_max()
                    print('At Max')
    except KeyboardInterrupt:
        print('Cleaning up')
        for s in servos:
            s.disable()

main()