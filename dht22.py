# tracker.py
# Helper class that fetches data from our dht22 sensor
# uses adafruit_dht ❤️ https://github.com/adafruit/Adafruit_CircuitPython_DHT

# Pi imports
import adafruit_dht

class DHT22():
    # Helper class
    def __init__(self, Pin):
        self.pin = Pin
        self.dht_device = adafruit_dht.DHT22(self.pin)

    def fetch_data(self):
        temperature = None
        humidity = None
        retries = 0
        while temperature == None or humidity == None:
            if retries > 10: # Try 10 times and then return None
                break
            try:
                temperature = self.dht_device.temperature
                humidity = self.dht_device.humidity
            except:
                retries += 1
        return (temperature, humidity)