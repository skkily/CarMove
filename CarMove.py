#!/usr/bin/python
#控制小车移动的库
import serial
import math

# 左前 右前 左后  右后

class CarMove():


    def __init__(self):
        # create a default object, no changes to I2C address or frequency
        self.port = "/dev/ttyUSB0"
        self.serialFromArduino = serial.Serial(self.port, 9600)
        # 打开串口, 连接到Arduino上
        self.serialFromArduino.flushInput()
        print("小车初始化完成...")

###########     61：停止   62：前转      63：后转

    def func(self,speed):
        return bytes(bytearray([int(hex(speed),16)]))




    def stop(self):     #停止
        self.serialFromArduino.write(bytes.fromhex('61'))
        self.serialFromArduino.write(bytes.fromhex('96'))
        self.serialFromArduino.write(bytes.fromhex('61'))
        self.serialFromArduino.write(bytes.fromhex('96'))
        self.serialFromArduino.write(bytes.fromhex('61'))
        self.serialFromArduino.write(bytes.fromhex('96'))
        self.serialFromArduino.write(bytes.fromhex('61'))
        self.serialFromArduino.write(bytes.fromhex('96'))
        self.serialFromArduino.write(bytes.fromhex('ff'))


    def forWord(self):  #前进
        self.serialFromArduino.write(bytes.fromhex('62'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('62'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('62'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('62'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('ff'))

    def back(self):     #后退
        self.serialFromArduino.write(bytes.fromhex('63'))
        self.serialFromArduino.write(bytes.fromhex('93'))
        self.serialFromArduino.write(bytes.fromhex('63'))
        self.serialFromArduino.write(bytes.fromhex('93'))
        self.serialFromArduino.write(bytes.fromhex('63'))
        self.serialFromArduino.write(bytes.fromhex('93'))
        self.serialFromArduino.write(bytes.fromhex('63'))
        self.serialFromArduino.write(bytes.fromhex('93'))
        self.serialFromArduino.write(bytes.fromhex('ff'))


    def turnRound(self,direction):      #自转
        if direction:        #顺时针（左侧：前，右侧：后）
            print("顺时针自转...")
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(bytes.fromhex('60'))
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(bytes.fromhex('60'))
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(bytes.fromhex('60'))
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(bytes.fromhex('60'))
            self.serialFromArduino.write(bytes.fromhex('ff'))
        else:   #逆时针
            print("逆时针自转...")
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(bytes.fromhex('60'))
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(bytes.fromhex('60'))
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(bytes.fromhex('60'))
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(bytes.fromhex('60'))
            self.serialFromArduino.write(bytes.fromhex('ff'))

    def sidewaysR(self): #向右平移 （左前：前，右前：后，左后：后，右后：前）
        print("向右平移...")
        self.serialFromArduino.write(bytes.fromhex('62'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('63'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('63'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('62'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('ff'))

    def sidewaysL(self): #向左平移 （左前：后，右前：前，左后：前，右后：后）
        print("向左平移...")
        self.serialFromArduino.write(bytes.fromhex('63'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('62'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('62'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('63'))
        self.serialFromArduino.write(bytes.fromhex('92'))
        self.serialFromArduino.write(bytes.fromhex('ff'))

    def turnR(self,angle):
        print("右转...")
        if 5<angle<85:#右后
            a=(90-angle)/2
            b=int((math.pi/180*a*2*5+0.5)*1.5)
            c = self.func(b+130)
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(self.func(70))
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(c)
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(self.func(70))
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(c)
            self.serialFromArduino.write(bytes.fromhex('ff'))
        elif 275<angle<355:#右前
            a=(angle-270)/2
            b=int((math.pi/180*a*2*5+0.5)*1.5)
            c = self.func(b+130)
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(self.func(70))
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(c)
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(self.func(70))
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(c)
            self.serialFromArduino.write(bytes.fromhex('ff'))




    def turnL(self,angle):
        print("左转...")
        if 185<angle<265:#左前
            a=(angle-180)/2
            b=int((math.pi/180*a*2*5+0.5)*1.5)
            c = self.func(b+130)
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(c)
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(self.func(70))
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(c)
            self.serialFromArduino.write(bytes.fromhex('62'))
            self.serialFromArduino.write(self.func(70))
            self.serialFromArduino.write(bytes.fromhex('ff'))
        elif 95<angle<175:#左后
            a=(angle-90)/2
            b=int((math.pi/180*a*2*5+0.5)*1.5)
            c = self.func(b+130)
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(c)
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(self.func(70))
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(c)
            self.serialFromArduino.write(bytes.fromhex('63'))
            self.serialFromArduino.write(self.func(70))
            self.serialFromArduino.write(bytes.fromhex('ff'))


    def move(self,angle):
        #if
        angle=float(angle)
        print("移动")
        if 265<=angle<=275:#前进
            self.forWord()
        elif 85<=angle<=95:#后退
            self.back()
        elif angle==361:#停止
            self.stop()
        elif angle==666:
            self.turnRound(True)
        elif angle==888:
            self.turnRound(False)
        # elif 175<=angle<=185:#向左平移
        #     self.sidewaysL()
        # elif 355<=angle<=360 and 0<=angle<=5:#向右平移
        #     self.sidewaysR()
        elif 5<angle<85:#右后
            self.turnR(angle)
        elif 275 < angle < 355:  # 右前
            self.turnR(angle)
        elif 185<angle<265:#左前
            self.turnL(angle)
        elif 95 < angle < 175:  # 左后
            self.turnL(angle)



