import serial
import time
import sys
from datetime import datetime
import numpy as np
import csv
from csv import writer

#setup serials for the testing rig and microphone array
TRport = '/dev/ttyACM1'
MAport = '/dev/ttyACM0'

def serialReceive(port, bits): #check and make sure it works
    input = np.array()
    with serial.Serial(port, 9600, stopbits=None) as ser:
        for i in range(0, sampleWindow):
            input.append(ser.read(bits), axis=0)
    return input

def serialSend(port, message):
    with serial.Serial(port, baudrate = 9600) as ser:
        ser.write(message)#wait extra long for device to be ready
        ser.write(message)#unsure if voltage drop is issue

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
    a = 0
    with serial.Serial(TRport, baudrate = 9600) as tr:
        with serial.Serial(MAport, baudrate=1152000) as ma:
            time.sleep(1)
            for i in range(0,600):
                time.sleep(0.5)
                tr.write(b'1') #move tr
                time.sleep(0.5)
                tr.write(b'0') # play sound from TR after delay
                name = './test.csv'
                rf = []
                rb = []
                lf = []
                lb = []
                print('connected')
                ma.write(b'1')  # tell to start recording
                time.sleep(0.05)
                a = 0
                count = 0
                while count < 1000:
                    a = ma.readline()
                    rf.append(ma.readline())
                    rb.append(ma.readline())
                    lf.append(ma.readline())
                    lb.append(ma.readline())
                    count += 1

                quadrant = 0
                eight = 0
                if i in range(1, 101):
                    quadrant = 1
                    if i < 51:
                        eight = 1
                    else:
                        eight = 2
                elif i in range(101, 201):
                    quadrant = 2
                    if i < 151:
                        eight = 3
                    else:
                        eight = 4
                elif i in range(201, 301):
                    quadrant = 3
                    if i < 251:
                        eight = 5
                    else:
                        eight = 6
                elif i in range(301, 401):
                    quadrant = 4
                    if i < 351:
                        eight = 7
                    else:
                        eight = 8

                with open(name, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow(rf + rb + lf + lb + [i] + [quadrant] + [eight])

                print(count)

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




#tasks

#send priming bit to MA and testing rig, telling them to go
#then wait for responding data on the arduino to come back
#once received, restart
