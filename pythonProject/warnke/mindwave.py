from PyNeuro.PyNeuro import PyNeuro
from time import sleep

pn = PyNeuro()
pn.s
pn.start()
while True:
    print(pn.status)
    if pn.meditation > 70: # Access data through object
        pn.close()
    sleep(0.2)