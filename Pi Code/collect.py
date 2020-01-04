import serial
from datetime import datetime
import numpy as np
import csv
from csv import writer

#setup serials for the testing rig and microphone array
TRport = '/dev/ttyACMO'
MAport = '/dev/ttyACMO'
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
    serialSend(TRport, bin(1))//send to forward
    serialSend(TRport, bin(1))//send one step
    # send bit to MA, wait for response
    # once received
    bool MAres = serialHS(check, True, MAport, check)
    if MAres:
        return

    # send priming bit to MA and testing rig, telling them to go
    # then wait for responding data on the arduino to come back
    # once received, restart
    serialSend('prime', TRport)
    serialSend('prime', MAport)
    return serialReceive(MAport, bits)

def serialReceive(port, bits):
    input = np.array()
    with serial.Serial(port, 9600) as ser:
        for i in range(0, sampleWindow):
            input.append(ser.read(bits), axis=0)
    return input

def serialSend(message, port):
    with serial.Serial(port, 9600) as ser:
        ser.write(message)

def serialHS(message, needsCheck, port, expected):#handshake
    bool quit = False
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
            else
                quit = False
        else:
            quit = False
    return quit

if __name__ == '__init__':
    sample_data = collect(10)
    name = './test.csv'
    with open(name,'w', newline='') as csv:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow(sample_data)



#tasks

#send priming bit to MA and testing rig, telling them to go
#then wait for responding data on the arduino to come back
#once received, restart
