# import paho.mqtt.client as mqtt
# import time

# def on_connect(client, userdata, rc):
#     client.subscribe("Gahao/feeds/feed")
#     client.publish("Gahao/feeds/feed","Now")
#     time.sleep(4)

# def on_message(client, userdata, msg):
#     # Do something
#     pass
# try:
#     client = mqtt.Client()
#     client.on_connect = on_connect
#     client.on_message = on_message
#     broker_address = "192.168.1.184"

#     client.connect(broker_address)
# except:
#     pass