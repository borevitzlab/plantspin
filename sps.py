

#__author__ = 'Jared Streich and Kevin Murray'
#__version__ = '2983474627822723646378273647280.9001.2 and a half'
#__date__ = 'August, 6 2013'
#Citation at bottom, mostly from Phidgets etc.


#Basic imports
from ctypes import *
import sys
from time import sleep
#Phidget specific imports
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, CurrentChangeEventArgs, PositionChangeEventArgs, VelocityChangeEventArgs
from Phidgets.Devices.AdvancedServo import AdvancedServo
from Phidgets.Devices.Servo import ServoTypes
import os

#Create an advancedServo object
try:
    advancedServo = AdvancedServo()
except RuntimeError as e:
    print("Runtime Exception: %s" % e.details)
    print("Exiting....")
    exit(1)

#stack to keep current values in
currentList = [0,0,0,0,0,0,0,0]
velocityList = [0,0,0,0,0,0,0,0]

#Information Display Function
def DisplayDeviceInfo():
    print("|------------|----------------------------------|--------------|------------|")
    print("|- Attached -|-              Type              -|- Serial No. -|-  Version -|")
    print("|------------|----------------------------------|--------------|------------|")
    print("|- %8s -|- %30s -|- %10d -|- %8d -|" % (advancedServo.isAttached(), advancedServo.getDeviceName(), advancedServo.getSerialNum(), advancedServo.getDeviceVersion()))
    print("|------------|----------------------------------|--------------|------------|")
    print("Number of motors: %i" % (advancedServo.getMotorCount()))

#Event Handler Callback Functions
def Attached(e):
    attached = e.device
    print("Servo %i Attached!" % (attached.getSerialNum()))

def Detached(e):
    detached = e.device
    print("Servo %i Detached!" % (detached.getSerialNum()))

def Error(e):
    try:
        source = e.device
        print("Phidget Error %i: %s" % (source.getSerialNum(), e.eCode, e.description))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))

def CurrentChanged(e):
    global currentList
    currentList[e.index] = e.current

def PositionChanged(e):
    source = e.device
    print("AdvancedServo %i: Motor %i Position: %f - Velocity: %f - Current: %f" % (source.getSerialNum(), e.index, e.position, velocityList[e.index], currentList[e.index]))
    if advancedServo.getStopped(e.index) == True:
        print("Motor %i Stopped" % (e.index))

def VelocityChanged(e):
    global velocityList
    velocityList[e.index] = e.velocity

#Main Program Code

#set up our event handlers
try:
    advancedServo.setOnAttachHandler(Attached)
    advancedServo.setOnDetachHandler(Detached)
    advancedServo.setOnErrorhandler(Error)
    advancedServo.setOnCurrentChangeHandler(CurrentChanged)
    advancedServo.setOnPositionChangeHandler(PositionChanged)
    advancedServo.setOnVelocityChangeHandler(VelocityChanged)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

print("Opening phidget object....")

try:
    advancedServo.openPhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

print("Waiting for attach....")

try:
    advancedServo.waitForAttach(10000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    try:
        advancedServo.closePhidget()
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Exiting....")
        exit(1)
    print("Exiting....")
    exit(1)
else:
    DisplayDeviceInfo()

try:
    print("Setting the servo type for motor 0 to HITEC_HS322HD")
    advancedServo.setServoType(0, ServoTypes.PHIDGET_SERVO_HITEC_HS322HD)
    #Setting custom servo parameters example - 600us-2000us == 120 degrees, velocity max 1500
    #advancedServo.setServoParameters(0, 600, 2000, 120, 1500)
    print("Speed Ramping state: %s" % advancedServo.getSpeedRampingOn(0))
    print("Stopped state: %s" % advancedServo.getStopped(0))
    print("Engaged state: %s" % advancedServo.getEngaged(0))
    
    print("Working with motor 0 only...")
        
    print("Engage the motor...")
    advancedServo.setEngaged(0, True)
    sleep(2)
    
    print("Engaged state: %s" % advancedServo.getEngaged(0))
    
    print("Move to position PositionMax...")
    advancedServo.setPosition(0, advancedServo.getPositionMax(0))
    sleep(10)

    fh = open("/Users/u5212257/trigger", "w")
    fh.write("a")
    fh.close()
    sleep(0.5)
	
    print("Move to position Check 1")
    advancedServo.setServoParameters(0, 800, 1600, 330, 25)
    sleep(10)
    
    print("Move to position PositionMin...")
    advancedServo.setPosition(0, advancedServo.getPositionMin(0))
    sleep(10)
    
    print("Disengage the motor...")
    advancedServo.setEngaged(0, False)
    sleep(2)
    
    print("Engaged state: %s" % advancedServo.getEngaged(0))
    
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    try:
        advancedServo.closePhidget()
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Exiting....")
        exit(1)
    print("Exiting....")
    exit(1)

print("Closing...")

try:
    advancedServo.closePhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

os.unlink("/Users/u5212257/trigger")

print("Done.")
exit(0)

#Modified from:
#"""Copyright 2010 Phidgets Inc.
#This work is licensed under the Creative Commons Attribution 2.5 Canada License. 
#To view a copy of this license, visit http://creativecommons.org/licenses/by/2.5/ca/
#"""

#__author__ = 'Adam Stelmack'
#__version__ = '2.1.8'
#__date__ = 'May 17 2010'

fh = open("/Users/u5212257/Desktop, "w")
    fh.write("a")
    fh.close()
    sleep(0.5)