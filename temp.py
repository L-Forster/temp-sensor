import time
import board
import adafruit_dht
from pushbullet import PushBullet
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

dhtDevice = adafruit_dht.DHT22(board.D12, use_pulseio=False)
access_token = ""

while True:
    try:
        temperature_c = dhtDevice.temperature

        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} C    Humidity: {} ".format(
                temperature_c, humidity
            )
            
        )
        f = open("Temp Data.txt", "a")
        f.write("Temp: " + str(temperature_c) + " Humidity: "+ str(humidity) +"\n")
        f.close()
        if temperature_c > 35:
            file = "message.txt"
            with open(file, mode="r" ) as f2:
                text = f2.read()
            print("Exceeded maximum temperature")
            pb = PushBullet(access_token)
            push = pb.push_note("Temperature Warning",text)
            
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(300)

