import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
pwm=GPIO.PWM(27,100)
pwm.start(0)

try:
    while 1:
        print("Rising")
        for x in range(100):
            pwm.ChangeDutyCycle(x)
            time.sleep(0.01)
        print("Decresing")
        for x in range(100,0,-1):
            pwm.ChangeDutyCycle(x)
            time.sleep(0.01)
            

except:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
