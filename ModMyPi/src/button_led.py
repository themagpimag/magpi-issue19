import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
while True:
    input_value = GPIO.input(17)
    if input_value == False:
        print("Who pressed my button?")
        for x in range(0, 3):
            GPIO.output(18, True)
            time.sleep(1)
            GPIO.output(18, False)
            time.sleep(1)            
        while input_value == False:
            input_value = GPIO.input(17)
            
            
