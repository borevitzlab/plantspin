#!/usr/bin/env python



#__author__ = 'Jared Streich and Kevin Murray'
#__version__ = '0.9001.2'
#__date__ = 'August, 6 2013'
#Citation at bottom, mostly from Phidgets etc.

#Basic imports
from ctypes import *
import sys
import random
#Phidget specific imports
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, InputChangeEventArgs, OutputChangeEventArgs, SensorChangeEventArgs
from Phidgets.Devices.InterfaceKit import InterfaceKit
from Phidgets.PhidgetLibrary import PhidgetLibrary
from time import sleep
import os

#Create an interfacekit object
try:
    interfaceKit = InterfaceKit()
except RuntimeError as e:
    print("Runtime Exception: %s" % e.details)
    print("Exiting....")
    exit(1)

#Information Display Function
def displayDeviceInfo():
    print("|------------|----------------------------------|--------------|------------|")
    print("|- Attached -|-              Type              -|- Serial No. -|-  Version -|")
    print("|------------|----------------------------------|--------------|------------|")
    print("|- %8s -|- %30s -|- %10d -|- %8d -|" % (interfaceKit.isAttached(), interfaceKit.getDeviceName(), interfaceKit.getSerialNum(), interfaceKit.getDeviceVersion()))
    print("|------------|----------------------------------|--------------|------------|")
    print("Number of Digital Inputs: %i" % (interfaceKit.getInputCount()))
    print("Number of Digital Outputs: %i" % (interfaceKit.getOutputCount()))
    print("Number of Sensor Inputs: %i" % (interfaceKit.getSensorCount()))

def AttachHandler(event):
    attachedDevice = event.device
    serialNumber = attachedDevice.getSerialNum()
    deviceName = attachedDevice.getDeviceName()
    print("Hello to Device " + str(deviceName) + ", Serial Number: " + str(serialNumber))
    attachedDevice = device
    
#Event Handler Callback Functions
def interfaceKitAttached(e):
    attached = e.device
    print("InterfaceKit %i Attached!" % (attached.getSerialNum()))

def interfaceKitDetached(e):
    detached = e.device
    print("InterfaceKit %i Detached!" % (detached.getSerialNum()))

def interfaceKitError(e):
    try:
        source = e.device
        print("InterfaceKit %i: Phidget Error %i: %s" % (source.getSerialNum(), e.eCode, e.description))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))

def interfaceKitInputChanged(e):
    source = e.device
    print("InterfaceKit %i: Input %i: %s" % (source.getSerialNum(), e.index, e.state))

def interfaceKitSensorChanged(e):
    source = e.device
    print("InterfaceKit %i: Sensor %i: %i" % (source.getSerialNum(), e.index, e.value))

def interfaceKitOutputChanged(e):
    source = e.device
    print("InterfaceKit %i: Output %i: %s" % (source.getSerialNum(), e.index, False))

#Main Program Code
try:
    interfaceKit.setOnAttachHandler(interfaceKitAttached)
    interfaceKit.setOnDetachHandler(interfaceKitDetached)
    interfaceKit.setOnErrorhandler(interfaceKitError)
    interfaceKit.setOnInputChangeHandler(interfaceKitInputChanged)
    interfaceKit.setOnOutputChangeHandler(interfaceKitOutputChanged)
    interfaceKit.setOnSensorChangeHandler(interfaceKitSensorChanged)

except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

print("Opening phidget object....")

try:
    interfaceKit.openPhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

print("Wait max: 10 seconds...")

try:
    interfaceKit.waitForAttach(10000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    try:
        interfaceKit.closePhidget()
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Exiting....")
        exit(1)
    print("Exiting....")
    exit(1)
else:
    displayDeviceInfo()


#def AttachHandler(event):
#    attachedDevice = device
#    serialNumber = attachedDevice.getSerialNum()
#    deviceName = attachedDevice.getDeviceName()
#    print("Hello to Device " + str(deviceName) + ", Serial Number: " + str(serialNumber))

try:
   while not os.path.exists("/Users/u5212257/trigger"):
       sleep(0.05)
       print ".",
       sys.stdout.flush()
   print("Starting Camera_repeat_script.py")
   for iii in xrange(30):
       print iii+1
       interfaceKit.setOutputState (7, True)
       interfaceKit.setOutputState (0, True)
       sleep(0.38)
   
       interfaceKit.setOutputState (7, False)
       interfaceKit.setOutputState (0, False)
       sleep(0.38)

except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))

print("Setting the data rate for each sensor index to 16ms....")
for i in range(interfaceKit.getSensorCount()):
    try:
        
        interfaceKit.setDataRate(0, 16)
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))

print("Closing program")

try:
    interfaceKit.closePhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

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
