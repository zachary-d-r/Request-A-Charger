#connecting raspbery pi to arduino 

import serial,time

lockerDictionary = {'Locker 1':4, 'Locker 2':9, 'Locker 3':13} #dictionary defining lockers to pin numbers


    
with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino: #opening a serial connecting with the arduino 
    time.sleep(0.1) #wait for serial to open
    if arduino.isOpen(): #if we connected to the arudino 
        print("{} connected!".format(arduino.port))
        time.sleep(5)
        arduino.write('good morning'.encode()) #sending a message to the arudino to make sure the connection works. This can be taken out
        time.sleep(5)
        try:
            while True:
                cmd=input("Enter Command: ") #user input to enter a command. command should either be: open or close followed by locker #
                print('sending command')
                arduino.write(cmd.lower().encode()) #writing the command to the arduino. The arduino will slice the command.
                while arduino.inWaiting()==0: pass
                if  arduino.inWaiting()>0: 
                    answer=arduino.readline() #read the arudino serial monitor
                    print(answer)
                    arduino.flushInput() #remove data after reading
        except KeyboardInterrupt:
            print("Ending Program")
