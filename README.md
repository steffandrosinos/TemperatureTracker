# <p align="center">Raspberry Pi Python Temperature Tracker</p>
<img src="https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/0350600d-5abe-44b0-a0d6-502efc81cc45" align="right"
     alt="Example MySQL data" width="500" height="220">
<br><br>Simple Raspberry Pi Temperature tracker for my room. Backend is a python script that stores the temperature from a dht22 sensor in a MySQL database (stores 1,440 mesurements per day). Runs every minute via a cronjob.
<br><br>
## Requirements
 - Raspberry Pi
 - dht22 sensor
 - python3
   - adafruit-python-shell
   - Adafruit_CircuitPython_DHT - https://github.com/adafruit/Adafruit_CircuitPython_DHT
   - PyMySQL - https://github.com/PyMySQL/PyMySQL

## Database setup<br>
The database this project uses is MySQL with python integration via [PyMySQL](https://github.com/PyMySQL/PyMySQL). The table name that you push data to can be configured in the config file. The table should be created with the followingbut can be created how you wish. Just note that you might need to change definitions in database.py to suite your needs.
```MySQL
CREATE TABLE `newtable` (
  `dateunix` varchar(64) NOT NULL,
  `datestr` DATETIME NOT NULL,
  `temperature` DECIMAL(6,1) NOT NULL,
  `humidity` VARCHAR(8) NOT NULL
);
```

Example data
![image](https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/a45c617f-b030-4162-a505-4f915ee8927b)

Config file
![image](https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/80e38d37-328e-4edc-b44e-156aa74d7084)


Crontab command:
* * * * * cd /home/steffan/TemperatureTracker && /usr/bin/python3.11 ./tracker.py --config="./config.ini" 2>&1

