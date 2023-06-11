# Temperature Tracker
Raspberry Pi Temperature tracker for my room. Backend is a python script that stores the temperature from a dht22 sensor and stores data in MySQL every minute.

This project uses the following repos
 - Adafruit_CircuitPython_DHT - https://github.com/adafruit/Adafruit_CircuitPython_DHT

## DB setup<br>
![image](https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/a449abf9-e1b4-453c-8a8b-e95450d17560)

Example data
![image](https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/a45c617f-b030-4162-a505-4f915ee8927b)

Config file
![image](https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/80e38d37-328e-4edc-b44e-156aa74d7084)


Crontab command:
* * * * * cd /home/steffan/TemperatureTracker && /usr/bin/python3.11 ./tracker.py --config="./config.ini" 2>&1

