import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

stepPin1=31
stepPin2=33
stepPin3=35
stepPin4=37


GPIO.setup(stepPin1, GPIO.OUT)
GPIO.setup(stepPin2, GPIO.OUT)
GPIO.setup(stepPin3, GPIO.OUT)
GPIO.setup(stepPin4, GPIO.OUT)

GPIO.output(stepPin1, False)
GPIO.output(stepPin2, False)
GPIO.output(stepPin3, False)
GPIO.output(stepPin4, False)


def singlestep(s1, s2, s3, s4):
    GPIO.output(stepPin1, s1)
    GPIO.output(stepPin2, s2)
    GPIO.output(stepPin3, s3)
    GPIO.output(stepPin4, s4)
    

def clockwiserotate(delay, steps):
    print("Clock wise - ")
    for i in range(0,steps):        
        singlestep(1,0,0,0)
        time.sleep(delay)
        singlestep(1,1,0,0)
        time.sleep(delay)
        singlestep(0,1,0,0)
        time.sleep(delay)
        singlestep(0,1,1,0)
        time.sleep(delay)
        singlestep(0,0,1,0)
        time.sleep(delay)
        singlestep(0,0,1,1)
        time.sleep(delay)
        singlestep(0,0,0,1)
        time.sleep(delay)
        singlestep(1,0,0,1)
        time.sleep(delay)

def anticlockwiserotate(delay, steps):
    print("Anti Clock wise - ")
    for i in range(0,steps):
        singlestep(1,0,0,1)
        time.sleep(delay)
        singlestep(0,0,0,1)
        time.sleep(delay)
        singlestep(0,0,1,1)
        time.sleep(delay)
        singlestep(0,0,1,0)
        time.sleep(delay)
        singlestep(0,1,1,0)
        time.sleep(delay)
        singlestep(0,1,0,0)
        time.sleep(delay)
        singlestep(1,1,0,0)
        time.sleep(delay)
        singlestep(1,0,0,0)
        time.sleep(delay)


try:
    delay = 1/1000
    steps=21
    for x in range(1,25) :
        clockwiserotate(delay, steps)
    #print("Wait a sec...");
    
    #for x in range(1,25) :
     #   anticlockwiserotate(delay, steps)
        
    

finally:
    GPIO.cleanup()
