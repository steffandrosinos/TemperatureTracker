# TemperatureTracker
Raspberry Pi Temperature tracker for my room. Backend is a python script that stores the temperature from a dht22 sensor and stores data in MySQL every minute. Front-end is a flask app hosted with apache2.

DB setup<br>
![image](https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/a449abf9-e1b4-453c-8a8b-e95450d17560)

Example data
![image](https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/a45c617f-b030-4162-a505-4f915ee8927b)


Crontab command:
* * * * * cd /home/steffan/TemperatureTracker && /usr/bin/python3.11 ./tracker.py --config="./config.ini" 2>&1

