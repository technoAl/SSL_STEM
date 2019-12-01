import serial
from datetime import datetime

#setup serials for the testing rig and microphone array
TRport = '/dev/ttyACMO'
MAport = '/dev/ttyACMO'

check = 'ch'

def collect(angle, increment):
    # for each angle, send angle to TR
    # wait for response from TR
    # once received, if TR went to specified angle
    bool TRres = serialTR(angle, True)
    if TRres:
        return

    # send bit to MA, wait for response
    # once received
 

def serialTR(message, needsCheck, port, expected):
    bool quit = False
    with serial.Serial(port, 9600) as ser:
        ser.write(bin(message))
        print('--------------------------')
        print('-----TR Message SENT!-----')
        print('--------------------------')
        if needsCheck:
            SERprimerBit = ser.read(timeout = 5)
            if SERprimerBit == None:
                print('--------------------------')
                print('----TR Receiving ERROR----')
                print('--------------------------')
                quit = True
            elif SERprimerBit != expected:
                print('--------------------------')
                print('----??????????????????----')
                print('--------------------------')
                quit = True
            else
                quit = False
        else:
            quit = False
    return quit

if __name__ == '__init__':


#tasks

#send priming bit to MA and testing rig, telling them to go
#then wait for responding data on the arduino to come back
#once received, restart
