import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("192.168.20.93", 1883, 60)
client.publish("maple/word",'1')