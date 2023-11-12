import mindwave, time
from pprint import pprint

headset = mindwave.Headset('/dev/tty.MindWaveMobile','C9B2')

time.sleep(2)

headset.connect()
print ("Connecting...")
#
while headset.status != 'connected':
     time.sleep(0.5)
     if headset.status == 'standby':
         headset.connect()
         print ("Retrying connect...")
print ("Connected.")
from NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy()

def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of attention is: ", attention_value)
    return None

neuropy.setCallBack("attention", attention_callback)
neuropy.start()

try:
    while True:
        sleep(0.2)
finally:
    neuropy.stop()
