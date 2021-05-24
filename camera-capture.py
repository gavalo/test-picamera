from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(2)

# Try custom resolution
#camera.resolution = (1280, 720)

# Try maximum resolution (supported by this camera module)
#camera.resolution = (2592, 1944)

file_name = "/home/pi/test-picamera/images/img_" + str(time.time()) + ".jpg"
camera.capture(file_name)
print("Done.")
