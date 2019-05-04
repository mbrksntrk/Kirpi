# Libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Distance sensor GPIO Pins
DIST_TRIGGER = 23
GPIO.setup(DIST_TRIGGER, GPIO.OUT)
DIST_ECHO = 24
GPIO.setup(DIST_ECHO, GPIO.IN)


def distance():
    # set Trigger to HIGH for 0.01ms
    GPIO.output(DIST_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(DIST_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(DIST_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(DIST_ECHO) == 1:
        StopTime = time.time()

    # calculate elapsed time and
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back

    time_elapsed = StopTime - StartTime
    distance = (time_elapsed * 34300) / 2

    return distance


if __name__ == '__main__':
    while True:
        dist = distance()
        print("Distance is %.1f centimeter" % dist)
        time.sleep(0.5)
