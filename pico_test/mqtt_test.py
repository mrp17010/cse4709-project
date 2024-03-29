import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

led = Pin("LED", Pin.OUT)

def sub_callback (topic, message):
    print(f'from {topic} got {message}') 
    led.value(int.from_bytes(message,'big')-48)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'patel'
password = ''
wlan.connect(ssid,password)

while wlan.isconnected() == False:
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi")

mqtt_host = 'io.adafruit.com'
mqtt_username = 'm_patel'
mqtt_password = ''
mqtt_topic = 'm_patel/feeds/test-mqtt'
mqtt_client_id = 'madhav_patel_test_mqtt'

client = MQTTClient(client_id = mqtt_client_id,
                         server = mqtt_host,
                         user = mqtt_username,
                         password = mqtt_password)


client.set_callback(sub_callback)
client.connect()
client.subscribe(mqtt_topic)
print("connected and subscribed")

try:
    while True:
        client.wait_msg()

except Exception as e:
    print("something went wrong")
    print(e)

finally:
    client.disconnect()
    print("disconnected")

