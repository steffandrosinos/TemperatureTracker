# TemperatureTracker
Raspberry Pi Temperature tracker for my room. Backend is a python script that stores the temperature from a dht22 sensor and stores data in MySQL every minute. Front-end is a flask app hosted with apache2.

Crontab command;
* * * * * cd /home/steffan/TemperatureTracker && /usr/bin/python3.11 ./tracker.py --config="./config.ini" 2>&1

