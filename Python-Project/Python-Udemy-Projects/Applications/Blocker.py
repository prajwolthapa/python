import time
from datetime import datetime as dt
hostpath_tmp = 'host'
redirect ="127.0.0.1"
website_list ={"www.facebook.com","www.google.com"}

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,0)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,3):
        with open(hostpath_tmp,'r+') as hostfile:
            content = hostfile.read()
            for website in website_list:
                if website in content :
                    pass
                else:
                    hostfile.write(redirect+'   '+website +'\n')
    else:
        with open(hostpath_tmp,'r+') as hosfile:
            file_content = hosfile.rea
    time.sleep(5);
