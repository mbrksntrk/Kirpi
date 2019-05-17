# Kirpi
_Ozyegin University CS350 Project_ by [mbrksntrk](https://www.github.com/mbrksntrk)

Simple ATIS system that broadcasts environmental temperature, humidity, proximity and light values via FM Radio and Telegram Channel. 

![Kipri](https://mburaks.com/kirpi/kirpi.png)

## Hardware
- Raspberry Pi 3 Model B+
- Sensors
    - Temperature & Humidity Sensor (DHT01)
    - Proximity Sensor (HC-SR04)
    - Light Sensor (LDR)
- Jumper cables & Breadboard
- Resistors 
- FM Receiver

## Software
- Python 3 
- Raspbian OS
- [PiFmRds](https://github.com/ChristopheJacquet/PiFmRds) For FM Transmitting

### Libraries
- [Adafruit_DHT](https://github.com/adafruit/Adafruit_Python_DHT)  Humidity and Temperature Library
- [gTTS](https://pypi.org/project/gTTS/) Google Text-To-Speech 
- [Sox](http://sox.sourceforge.net/sox.html) Sound library
