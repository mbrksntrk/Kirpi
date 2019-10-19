# Kirpi
_Ozyegin University CS350 Project_ by [mbrksntrk](https://www.github.com/mbrksntrk)

[![GitHub license](https://img.shields.io/github/license/mbrksntrk/Kirpi)](https://github.com/mbrksntrk/Kirpi/blob/master/LICENSE)
![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Fwww.mburaks.com%2Fkirpi%2Fkirpi.html)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fmbrksntrk%2FKirpi%2F)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fmbrksntrk%2FKirpi%2F)


Simple ATIS system that broadcasts environmental temperature, humidity, proximity and light values via FM Radio and Telegram Channel. 

![book](https://user-images.githubusercontent.com/32896514/67152519-a1a43480-f2e0-11e9-9c5a-d76ea3c987ea.png) **NEW! You can check-out the details of project on [Wiki Page](https://github.com/mbrksntrk/Kirpi/wiki) of this repository**

![t_logo](https://user-images.githubusercontent.com/32896514/67152273-29874000-f2db-11e9-8fb0-ce55f3360b0d.png) You can join Kirpi Telegram channel here: [t.me/kirpi](http://t.me/kirpi)

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
