# database.py
# Database Class for interacting with our MySQL database
# uses pymysql ❤️ https://github.com/PyMySQL/PyMySQL

from datetime import datetime
from pprint import pprint
import pymysql.cursors

class DB():
    def __init__(self, Host, Database, Table, User, Password):
        # Useful vars
        self.host = Host
        self.database = Database
        self.table = Table
        self.user = User
        self.password = Password

        # connection objects
        self.connection = None
        self.dbcursor = None
        self.connect()

    def connect(self):
        # Connect to our db via pymsql
        try:
            self.connection = pymysql.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                cursorclass = pymysql.cursors.DictCursor
            )
            self.dbcursor = self.connection.cursor()
        except Exception as e:
            pprint(e)
    
    def add_data(self, Temperature, Humidity):
        # Inputs:
        #   Temperature (float) - Mandatory
        #   Humidity    (float) - Mandatory
        # Database table will take in:
        #   "dateunix" varchar(64) [not null]
        #   "datestr" DATETIME [not null]
        #   "temperature" DECIMAL(6,1) [not null]
        #   "humidity" VARCHAR(8) [not null]

        # Fetch time now
        now = datetime.now()
        # The best datetime format is YYYY/MM/DD HH:MM:SS and you cant convince me otherwise
        datestr = now.strftime("%Y/%m/%d %H:%M:%S")
        unixtimestamp = int(now.timestamp())

        # Let's add % to humidity
        Humidity = f"{Humidity}%"

        sql = f"""
            INSERT INTO {self.database}.{self.table} VALUES (
                \"{str(unixtimestamp)}\",
                \"{str(datestr)}\",
                {Temperature},
                \"{Humidity}\"
            )
        """
        # Sent SQL query to db
        self.dbcursor.execute(sql) # exec sql
        self.connection.commit()   # commit changes
