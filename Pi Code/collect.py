import serial
import time
import sys
from datetime import datetime
import numpy as np
import csv
from csv import writer

#setup serials for the testing rig and microphone array
TRport = '/dev/ttyACM0'
#MAport = '/dev/ttyACMO'
sampleWindow = 100
bits = 10

check = 'ch'

def collect(steps):
    # for each angle, send angle to TR
    # wait for response from TR
    # once received, if TR went to specified angle
    # bool TRres = serialHS(angle, True, TRport, check)
    # if TRres:
    #     return
    serialSend(TRport, b'1')#send to forward
    print('someth')
    # send bit to MA, wait for response
    # once received
    # bool MAres = serialHS(check, True, MAport, check)
    # if MAres:
    #     return

    # send priming bit to MA and testing rig, telling them to go
    # then wait for responding data on the arduino to come back
    # once received, restart
    #serialSend('p', TRport) #p for prime
    # serialSend('r', MAport) #r for ready
    # return serialReceive(MAport, bits)

def serialReceive(port, bits): #check and make sure it works
    input = np.array()
    with serial.Serial(port, 9600) as ser:
        for i in range(0, sampleWindow):
            input.append(ser.read(bits), axis=0)
    return input

def serialSend(port, message):
    with serial.Serial(port, baudrate = 9600, timeout = 1) as ser:
        ser.write(message)
        time.sleep(5)
        ser.write(message)

def serialHS(message, needsCheck, port, expected):#handshake unsure if needed currently
    quit = False
    with serial.Serial(port, 9600) as ser:
        ser.write(bin(message))
        print('--------------------------')
        print('------ Message SENT! -----')
        print('--------------------------')
        if needsCheck:
            SERprimerBit = ser.read(timeout = 5)
            if SERprimerBit == None:
                print('--------------------------')
                print('----- Receiving ERROR ----')
                print('--------------------------')
                quit = True
            elif SERprimerBit != expected:
                print('--------------------------')
                print('----??????????????????----')
                print('--------------------------')
                quit = True
            else:
                quit = False
        else:
            quit = False
    return quit


if __name__ == '__main__':
    print('yo');
    collect(1)
    # for i in range(1,401):
    #     sample_data = collect(1)
    #     quadrant = 0
    #     eight = 0;
    #     if i in range(1, 101):
    #         quadrant = 1
    #         if i < 51:
    #             eight = 1
    #         else:
    #             eight = 2
    #     elif i in range(101, 201):
    #         quadrant = 2
    #         if i < 151:
    #             eight = 3
    #         else:
    #             eight = 4
    #     elif i in range(201, 301):
    #         quadrant = 3
    #         if i < 251:
    #             eight = 5
    #         else:
    #             eight = 6
    #     elif i in range(301, 401):
    #         quadrant = 4
    #         if i < 351:
    #             eight = 7
    #         else:
    #             eight = 8
    #
    #     name = './test.csv'
    #     with open(name,'w', newline='') as csv:
    #         writer = csv.writer(csvfile, delimiter=' ')
    #         writer.writerow(sample_data + quadrant + eighth + i)



#tasks

#send priming bit to MA and testing rig, telling them to go
#then wait for responding data on the arduino to come back
#once received, restart
