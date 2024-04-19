import network
import urequests
from time import sleep

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'patel'
password = ''
wlan.connect(ssid,password)

while wlan.isconnected() == False:
    print("waiting for connection...")
    sleep(1)

print(wlan.ifconfig())
print("\n\n2. Querying the current GMT+0 time:")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json())
