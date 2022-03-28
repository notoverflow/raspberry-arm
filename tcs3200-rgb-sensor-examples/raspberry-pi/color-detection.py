import RPi.GPIO as GPIO
import time

s2 = 19 # Raspberry Pi Pin 35
s3 = 13 # Raspberry Pi Pin 33
out = 26 # Pin 37

NUM_CYCLES = 10

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(out,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(s2,GPIO.OUT)
    GPIO.setup(s3,GPIO.OUT)

def read_value(a0, a1):
    GPIO.output(s2, a0)
    GPIO.output(s3, a1)

    # Give the sensor some time to adjust
    time.sleep(0.1)

    # Wait for a full cycle (this will make sure we only count full cycles)
    GPIO.wait_for_edge(out, GPIO.FALLING)
    GPIO.wait_for_edge(out, GPIO.RISING)

    start = time.time()

    GPIO.wait_for_edge(out, GPIO.FALLING)

    # The time that passed while we were waiting
    # for the out to change
    return (time.time() - start) * 1000000

def loop():
    while True:
        r = read_value(GPIO.LOW, GPIO.LOW)
        time.sleep(0.1)

        g = read_value(GPIO.HIGH, GPIO.HIGH)
        time.sleep(0.1)

        b = read_value(GPIO.LOW, GPIO.HIGH)

        if (b < g) and (b < r):
            print("Blue\n")
        elif (g < b) and (g < r):
            print("Green\n")
        elif (r < g) and (r < b):
            print("Red\n")

        time.sleep(1)

if __name__=='__main__':
    setup()

    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
