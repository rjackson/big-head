from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import json
import unit
import network
import ubinascii

from machine import WDT
from machine import Timer

MQTT_SERVER='192.168.86.24'
MQTT_PORT='1883'
MQTT_TOPIC='m5atom-env-sensor'

POLL_INTERVAL=10 # every 10 seconds  
WATCHDOG_TIMEOUT=30000
TICK_RESOLUTION=1000
  
wdt = WDT(timeout=WATCHDOG_TIMEOUT)
env3_1 = unit.get(unit.ENV3, unit.PORTA)
wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)
wlan_mac = wlan_sta.config('mac')
device_id = ubinascii.hexlify(wlan_mac).decode()

print("Device ID:", device_id)

m5mqtt = M5mqtt(device_id, MQTT_SERVER, MQTT_PORT)
m5mqtt.start()

tick = False
def tock(event):
  global tick
  tick = True

tim = Timer(0)
tim.init(period=POLL_INTERVAL * 1000, mode=Timer.PERIODIC, callback=tock)

while True:
  print("tick")
  if tick is True:
    m5mqtt.publish(MQTT_TOPIC, json.dumps({
      'temperature': env3_1.temperature,
      'humidity': env3_1.humidity,
      'pressure': env3_1.pressure,
      'device_id': device_id
    }))
    
    rgb.setColorAll(0xff0000)
    rgb.setBrightness(255)
    wait_ms(100)
    rgb.setBrightness(0)
    
    wdt.feed()
    print("tock")
    tick = False
    
  wait_ms(TICK_RESOLUTION)
