import RPi.GPIO as GPIO

led_pin = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

GPIO.output(led_pin, GPIO.LOW)
GPIO.cleanup()
