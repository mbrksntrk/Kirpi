# Libraries
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import signal
import sys
from gtts import gTTS
from ftplib import FTP
import os
import config
import requests
from datetime import datetime
import json

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
        humid, temp = Adafruit_DHT.read_retry(temp_sensor, temp_pin)  # Temperature and humidity

        # Create data array with values from sensors.
        data = {'date': str(datetime.now()), 'dist': distance(), 'temp': temp, 'humid': humid, 'light': light()}

        # Report in speaking language
        report = "Report: \n" \
                 "Distance is: {0:1.1f} centimeter. \n" \
                 "Temperature: {1:1.0f} celsius. \n" \
                 "Humidity: {2:1.0f}%." \
                 "\nLight level: {3}." \
            .format(data['dist'], data['temp'], data['humid'], data['light'])
        print(report)

        # Report in JSON format
        json_data = json.dumps(data)
        print(json_data)

        # Telegram Send Message by API
        requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(config.apikey),
                      data={'chat_id': config.chatid, 'text': report}).json()

        # Write to file
        file = open("report.html", "w")
        file.write(json_data)
        file.close()

        # Upload to FTP server
        ftp = FTP(config.ftphost)
        ftp.login(config.ftpuser, config.ftppass)
        with open('report.html', 'r') as f:
            ftp.storbinary('STOR %s' % 'kirpi.html', f)
        ftp.quit()

        # Report Text to Speech (gTTS Online)
        tts = gTTS(text=report, lang='en')
        tts.save("report.mp3")
        time.sleep(1)

        # FM Transmission
        os.system('sox -t mp3 report.mp3 -t wav - | sudo PiFmRds/src/pi_fm_rds -audio - -freq 77.0 -ps KIRPI-FM')

        # Delay between calculations
        time.sleep(1)

signal.pause()
