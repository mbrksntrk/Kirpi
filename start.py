# Libraries
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import signal
import sys
from gtts import gTTS
import os

GPIO.setmode(GPIO.BCM)

# Distance sensor config
DIST_TRIGGER = 23
GPIO.setup(DIST_TRIGGER, GPIO.OUT)
DIST_ECHO = 24
GPIO.setup(DIST_ECHO, GPIO.IN)

# Temp and Humidity sensor config
temp_sensor = Adafruit_DHT.DHT11
temp_pin = 4

# Light Sensor
ldr_pin = 3


def light():
    reading = 0
    GPIO.setup(ldr_pin, GPIO.OUT)
    GPIO.output(ldr_pin, GPIO.LOW)
    time.sleep(.1)

    GPIO.setup(ldr_pin, GPIO.IN)
    while GPIO.input(ldr_pin) == GPIO.LOW:
        reading += 1
    return 2000 / reading


def distance():
    # set Trigger to HIGH for 0.01ms
    GPIO.output(DIST_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(DIST_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    # save start_time
    while GPIO.input(DIST_ECHO) == 0:
        start_time = time.time()

    # save time of arrival
    while GPIO.input(DIST_ECHO) == 1:
        stop_time = time.time()

    # calculate elapsed time and
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back

    time_elapsed = stop_time - start_time
    return (time_elapsed * 34300) / 2


def signal_handler(sig, frame):
    print('You pressed Ctrl+C! Exiting...')
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':

    while True:
        report = "Report:\n"

        # Distance
        dist = distance()
        report += "Distance is: %d centimeter. \n" % dist

        # Temperature and humidity
        humidity, temperature = Adafruit_DHT.read_retry(temp_sensor, temp_pin)
        if humidity is not None and temperature is not None:
            report += "Temperature: {0:0.1f} celcius.  \nHumidity: {1:0.1f}%. \n".format(temperature, humidity)
        else:
            report += "Failed to get reading. Try agaidn\n"

        # Light
        light_val = light()
        report += "Light level: {}.".format(light_val)

        print(report)

        # Report Text to Speech (gTTS Online)
        tts = gTTS(text=report, lang='en')
        tts.save("report.mp3")
        time.sleep(1)

        # FM Transmission
        os.system('sox -t mp3 report.mp3 -t wav - | sudo PiFmAdv/src/pi_fm_adv --freq 77.0 --audio - --gpio 20 --ps '
                  'KIRPI-FM --rt \'M Burak Senturk - OzU CS350\' --pty 31 --wait 0')
        # Delay between calculations
        time.sleep(1)
        os.system('rm report.mp3')


signal.pause()
