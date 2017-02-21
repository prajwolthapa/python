import os
from datetime import datetime as dt
import time

route_ip ='127.0.0.1'
sites_disabled = ['www.cnn.com','www.google.com']
hostfile ='hosts'

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17) :
        with open(hostfile,'r+') as file:
            content = file.read()
            for website in sites_disabled:
                if website in content:
                    pass
                else:
                    file.write(route_ip+' '+website+'\n')

    else:
        print("Its fun time")
