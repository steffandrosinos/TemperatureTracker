# tracker.py
# Main tracker script, a cron job runs this every minute
# 1,440 entries per day

# our objects
from database import DB # database object
from dht22 import DHT22 # dht22 object

# Generic imports
from pprint import pprint
from board import D17 # our pin
import configparser
import argparse
import time

# Arg parser
parser = argparse.ArgumentParser()
parser.add_argument('--config', dest="config_location", default="/root/TemperatureTracker/config.ini", help="Config file for application")
args = parser.parse_args()

# Fetch config from file
config = configparser.ConfigParser()
config.read(args.config_location)
host = config["Database"]["Host"]
database = config["Database"]["database"]
table = config["Database"]["table"]
user = config["Database"]["user"]
password = config["Database"]["password"]

# Database object setup
database = DB(Host=host, Database=database, Table=table, User=user, Password=password)

# Current pinout setup
#   5V     - Pin 4
#   Data   - GPIO 17
#   ground - Pin 9
dht22 = DHT22(Pin=D17)
temperature, humidity = dht22.fetch_data() # fetch data
database.add_data(Temperature=temperature, Humidity=humidity) # add to db