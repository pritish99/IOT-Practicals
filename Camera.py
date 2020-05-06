import picamera
from time import sleep
camera=picamera.PiCamera()
camera.start_preview()
camera.start_recording('sample.h264') #to record a video
camera.wait_recording(5)
camera.stop_recording()
camera.capture("/home/pi/Desktop/Practicals/sample.jpg") #to click a picture
camera.stop_preview() # to stop the camera preview
