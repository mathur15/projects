import time
from datetime import datetime as dt
host_path = "/private/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","www.instagram.com","www.gmail.com","www.youtube.com","www.netflix.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13)< dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,22,15):
        #the current time should be in between the two dt datetime objects.
        print("Working hours")
        with open(host_path,'r+') as file:
            content = file.read()#read entire file
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        #if no time in between then we have to delete those lines we've written so that the host file is back to normal
        with open(host_path,'r+') as file:
            content = file.readlines()#store each line in a list
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    #equivalent to writing another for loop but done in line
                    file.write(line)
            file.truncate()#once all the new content is written
            #then all the old content is removed.

        print("fun hours")

    time.sleep(5)#stalls the next iteration by 5 seconds.
