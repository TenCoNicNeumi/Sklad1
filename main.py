#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import threading
import time

# novy komentar


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
r = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
Uss = UltrasonicSensor(Port.S4)
Cs = ColorSensor(Port.S3)
pas = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
Touch1 = TouchSensor(Port.S1)
Touch2 = TouchSensor(Port.S2)


DriveSpeedCalc = 300
DriveSpeed = DriveSpeedCalc
DriveSpeedNegated = DriveSpeed * (-1)


r.settings(-100000, 1000, 300, 700)


#=====FUNKCE===========================================================================================
def End():
    wait(90*1000)


def Wait(cas):
    wait(cas)


def Nabirani():
    global DriveSpeedNegated
    global DriveSpeed
    global DriveSpeedCalc
    global Aktivovano
    Aktivovano = True
    DriveSpeed = DriveSpeedCalc / 5
    DriveSpeedNegated = DriveSpeed * (-1)
    pas.run_until_stalled(10000, Stop.COAST,100)
    pas.run_until_stalled(-10000, Stop.HOLD, 100)
    DriveSpeed = DriveSpeedCalc
    DriveSpeedNegated = DriveSpeed * (-1)
    Aktivovano = False


def Wfollow(Distance):
    global DriveSpeedNegated
    global DriveSpeed
    global DriveSpeedCalc
    PROPORTIONAL_GAIN = 0.12
    DriveSpeedNegated = DriveSpeed * (-1)
    deviation = 0
    while Touch1.pressed() == False:
        while 60 <= Cs.reflection():
            if Touch1.pressed():
                break
            if (Distance - 50) < Uss.distance() and (Distance + 50) > Uss.distance():              
                deviation = Uss.distance() - Distance
            TurnRate = PROPORTIONAL_GAIN * deviation
            ev3.screen.clear()
            ev3.screen.print(deviation)
            r.drive(DriveSpeedNegated, TurnRate)
        TurnRate = PROPORTIONAL_GAIN * deviation
        r.drive(DriveSpeedNegated, TurnRate)
   
        thread = threading.Thread(target=Nabirani)
        thread.start()
        wait(120)





def WfollowCount(Distance):
    wait(200)
    global DriveSpeedNegated
    global DriveSpeed
    global DriveSpeedCalc
    DriveSpeed = 250
    PROPORTIONAL_GAIN = 0.4
    DriveSpeedNegated = DriveSpeed * (-1)
    deviation = 0
    for i in range(3):
        
        while 20 <= Cs.reflection():
            if Touch1.pressed():
                return
            if (Distance - 50) < Uss.distance() and (Distance + 50) > Uss.distance():              
                deviation = Uss.distance() - Distance
            TurnRate = PROPORTIONAL_GAIN * deviation
            ev3.screen.clear()
            ev3.screen.print(deviation)
            r.drive(DriveSpeedNegated, TurnRate)
        ev3.speaker.beep(100,100)
        TurnRate = PROPORTIONAL_GAIN * deviation
        r.drive(DriveSpeedNegated, TurnRate)
        thread = threading.Thread(target=Nabirani)
        thread.start()
        r.straight(15)


CaryCount = 0



def ThirdRun():
    global DriveSpeedNegated
    global DriveSpeed
    global DriveSpeedCalc
    global CaryCount
    global Aktivovano
    while CaryCount < 3:
        if Aktivovano == False:
            DriveSpeedNegated = DriveSpeed * (-1)


        if 50 >= Cs.reflection():
            DriveSpeedNegated = DriveSpeed / (-5)
            r.drive(DriveSpeedNegated, -5)
            thread = threading.Thread(target = Nabirani)
            thread.start()
            CaryCount = CaryCount + 1
            wait(500)
            '''if CaryCount == 3:
                r.stop()'''


        if Touch2.pressed() == True:
            r.drive(-40, 40)
            ev3.speaker.beep(800,1)
        else:
            r.drive(DriveSpeedNegated, -10)
            #wait(10)




   

def Rovnani():
    r. drive(100,0)
    wait(60)
    while True:
        if left_motor.speed() < 60:
            r.stop
            return
            break
'''
def WfollowSimple(Distance):
    wait(200)
    global DriveSpeedNegated
    global DriveSpeed
    global DriveSpeedCalc
    DriveSpeed = 100
    PROPORTIONAL_GAIN = 0.8
    DriveSpeedNegated = DriveSpeed * (-1)
    deviation = 0
    for i in range(3):
        #r.straight(50)
        while 20 <= Cs.reflection():
            if Touch1.pressed():
                return
            if (Distance - 50) < Uss.distance() and (Distance + 50) > Uss.distance():              
                deviation = Uss.distance() - Distance
            TurnRate = PROPORTIONAL_GAIN * deviation
            ev3.screen.clear()
            ev3.screen.print(deviation)
            r.drive(DriveSpeedNegated, TurnRate)
        ev3.speaker.beep(100,100)
        TurnRate = PROPORTIONAL_GAIN * deviation
        r.drive(DriveSpeedNegated, TurnRate)
'''
def RunToBall(Distance):
    global DriveSpeedNegated
    global DriveSpeed
    global DriveSpeedCalc
    global deviation
    DriveSpeed = 250
    PROPORTIONAL_GAIN = 1
    DriveSpeedNegated = DriveSpeed * (-1)
    deviation = 0
    for i in range(2):
        while Zluta < Cs.rgb()[2]:
            if Touch1.pressed():
                return
            if (Distance - 50) < Uss.distance() and (Distance + 50) > Uss.distance():              
                deviation = Uss.distance() - Distance
                TurnRate = PROPORTIONAL_GAIN * deviation
                ev3.screen.clear()
                ev3.screen.print(deviation)
                r.drive(DriveSpeedNegated, TurnRate)
            ev3.speaker.beep(100,100)
            TurnRate = PROPORTIONAL_GAIN * deviation
            r.drive(DriveSpeedNegated, TurnRate)


        

#======CODE========================================================================================

'''

while True:
    ev3.screen.print(Cs.rgb()[2])

'''

while not Touch2.pressed():
    wait(1)
Zluta = 60

pas.run_until_stalled(-1000000, Stop.HOLD, 150)
thread = threading.Thread(target = Nabirani)
thread.start()


r.drive(-100, 0)
wait(25)


ev3.speaker.play_notes(['C4/4', 'E4/4', 'G4/4'], 300)


Wfollow(445)
wait(150)
r.stop()


wait(10)
ev3.speaker.beep(500, 500)
ev3.speaker.beep(1200, 500)
#---PRVNI RADA HOTOVA---


r.straight(-110)
r.turn(-154)
pas.run_until_stalled(-10000, Stop.HOLD, 90)
#r.straight(325)
r.straight(100)

while True:
    while (Cs.rgb()[2]) > Zluta:
        r.drive(-160,0)
    wait(3)
    if (Cs.rgb()[2]) < Zluta:
        break

r.stop(Stop.HOLD)
#r.straight(30)
thread = threading.Thread(target=Nabirani)
thread.start()
r.turn(-173)


#r.straight(-25)
#r.turn(-38)         # Udelat tadz abz se to4il dokud nebude na spr8vn0 vyd8lenosti
ev3.speaker.beep(100, 100)
while not (333 <= Uss.distance()):
    r.turn(-2)
r.stop()

#r.straight(30)

WfollowCount(339)
#---DRUHA RADA HOTOVA---
while Touch1.pressed == False:
    r.drive(100,0)
r.stop()
r.straight(-40)
r.turn(140)
ev3.speaker.beep(1000,5)
if Touch2.pressed():
    r.turn(-10)
r.straight(60)
while True:
    while (Cs.rgb()[2]) > Zluta:
        r.drive(-160,-12)
        if Touch2.pressed():
            r.drive(-20, 40)
            ev3.speaker.beep(300, 2)

        
    wait(3)
    if (Cs.rgb()[2]) < Zluta:
        break


r.straight(7)

thread = threading.Thread(target=Nabirani)
thread.start()
#r.straight(-10)


r.turn(150)
ev3.speaker.beep(100,100)

ThirdRun()
r.stop()
#---TRETI RADA HOTOVA
r.turn(-40)
r.straight(30)

ev3.speaker.beep(200,2300)
r.straight(-100)
r.turn(337)

#WfollowSimple(30)
#left_motor.run_time(-100, 3, Stop.COAST, False)
#right_motor.run_time(-100, 3, Stop.COAST, False)
#r.straight(-110)
#r.speaker.beep(500, 3000)


#r.straight(950)

while Touch1.pressed() == False:
    r.drive(-200, 16)
    
    if 35 > Uss.distance():
        r.drive(-160, -30)
        ev3.speaker.beep(100, 100)
r.drive(-300,0)
wait(2000)
r.stop()
#r.straight(-10)
#r.turn(30)
#r.straight(10)

ev3.speaker.beep(300, 500)

r.straight(-60)


r.turn(-350)
while  50 < Cs.reflection():
    if Touch2.pressed() == True:
            r.drive(-150, 40)
            ev3.speaker.beep(800,1)
    else:
        r.drive(-200, -10)

r.turn(170)
r.drive(300,0)
wait(1500)
r.stop()

ev3.speaker.beep(200,200)
r.straight(50)
CaryCount = 0
while not CaryCount == 2:

    r.drive(-200, 12)
    
    if 300 > Uss.distance():
        r.drive(-120, -40)
        ev3.speaker.beep(200, 2)
    
    if Zluta > Cs.rgb()[2]:
        r.straight(10)
        CaryCount = CaryCount + 1

pas.run_until_stalled(10000, Stop.COAST, 90)
r.straight(50)
RunToBall(615)


#CaryCount = 0
#    while not CaryCount == 2:
 #       r.drive(-200, 12)
  #      
   #     if 570 > Uss.distance():
    #        r.drive(-100, -40)
     #       ev3.speaker.beep(160, 100)
      #  
       # if Zluta > Cs.rgb()[2]:
        #    r.straight(10)
         #   CaryCount = CaryCount + 1

r.straight(200)

pas.run_until_stalled(-10000, Stop.COAST, 100)
pas.run_until_stalled(-10000, Stop.COAST, 100)
#Nabany basketbl
r.straight(-50)
r.turn(175)
while True:
    while (Cs.rgb()[2]) > Zluta:
        r.drive(-200, -15)
        if 40 > Uss.distance():
            r.drive(-160, 20)
            ev3.speaker.beep(200, 100)
    wait(3)
    if (Cs.rgb()[2]) < Zluta:
        break


wait(400)
r.stop()


thread = threading.Thread(target=Nabirani)
thread.start()
r.turn(-180)
ev3.speaker.beep(500, 5000)