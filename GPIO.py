import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount=10
count=0
LEDPin1=27

GPIO.setup(LEDPin1,GPIO.OUT)

try:
    while count<blinkCount:
        GPIO.output(LEDPin1,1)
        print("LED ON")
        sleep(0.2)
        GPIO.output(LEDPin1,0)
        print("LED OFF")
        sleep(0.2)
        count+=1
finally:
    #Reset GPIO to safe state
    GPIO.cleanup()
