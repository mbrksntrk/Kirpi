# Libraries
import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)

# Distance sensor GPIO Pins
DIST_TRIGGER = 23
GPIO.setup(DIST_TRIGGER, GPIO.OUT)
DIST_ECHO = 24
GPIO.setup(DIST_ECHO, GPIO.IN)

# Temp and Humidity sensor config
temp_sensor = Adafruit_DHT.DHT11
temp_pin = 4


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
        # Distance
        dist = distance()
        print("Distance is %.1f centimeter" % dist)

        # Temperature and humidity
        humidity, temperature = Adafruit_DHT.read_retry(temp_sensor, temp_pin)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')

        # Delay between calculations
        time.sleep(0.5)