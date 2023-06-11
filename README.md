<!-- Made badly by steffan ❤️ -->
# <p align="center">Raspberry Pi Python Temperature Tracker</p>
<img src="https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/0350600d-5abe-44b0-a0d6-502efc81cc45" align="right"
     alt="Example MySQL data" width="460" height="200">
<br><br>Simple Raspberry Pi Temperature tracker for my room. Backend is a python script that stores the temperature from a dht22 sensor in a MySQL database (stores 1,440 mesurements per day). Runs every minute via a cronjob.
<br><br>
## Requirements
 - Raspberry Pi
 - dht22 sensor
 - python3
   - adafruit-python-shell - https://github.com/adafruit/Adafruit_Python_Shell
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
## Config file
<img src="https://github.com/steffandrosinos/TemperatureTracker/assets/39098140/cb59b3cf-54a2-4327-8e68-fe980cebc4c6" align="right"
     alt="Example MySQL data" width="304" height="220">
The script loads up a config file that has useful variables, the following variables are defined in the config:
 - **host**     - The hostname/address of your MySQL server
 - **database** - The database that your table resides in
 - **table**    - The table name that you want to store your data
 - **user**     - Login account for MySQL, should have access to the above database + table
 - **password** - The password for the login account
```ini
[Database]
host = localhost
database = yourdatabase
table = yourtable
user = youruser
password = userpassword
```
## How to run
For debugging, you can directly run the tracker.py script with the following. Make sure to include --config and point to your config.ini file.
```bash
python3 ./tracker.py --config="/path/to/config.ini"
```
I use a cronjob to run the script every minute. That's done with the following crontab -e entry. Make sure to setup the cronjob as root else our script won't have access to GPIO.
```cronjob
* * * * * cd /home/steffan/TemperatureTracker && /usr/bin/python3.11 ./tracker.py --config="./config.ini" 2>&1
```
<br><br>
<p align="center"><sub><b>made by steffan</b></sub></p>
<p align="center">❤️</p>
