# Libraries
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Distance sensor config
DIST_TRIGGER = 23
GPIO.setup(DIST_TRIGGER, GPIO.OUT)
DIST_ECHO = 24
GPIO.setup(DIST_ECHO, GPIO.IN)

# Temp and Humidity sensor config
temp_sensor = Adafruit_DHT.DHT11
temp_pin = 4

# Sound sensor config
mic_pin = 18
GPIO.setup(mic_pin, GPIO.IN)


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

        report = "\nReport:\n"

        # Distance
        dist = distance()
        report += "Distance is %.1f centimeter \n" % dist

        # Temperature and humidity
        humidity, temperature = Adafruit_DHT.read_retry(temp_sensor, temp_pin)
        if humidity is not None and temperature is not None:
            report += "Temperature is {0:0.1f}* \nHumidity is {1:0.1f}% \n".format(temperature, humidity)
        else:
            report += "Failed to get reading. Try again\n"

        # Sound
        if GPIO.input(mic_pin):
            report += "Alarm\n"
        else:
            report += "Sakin\n"

        print(report)
        # Delay between calculations
        time.sleep(1)