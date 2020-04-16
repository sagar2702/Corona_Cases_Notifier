from plyer import notification
from bs4 import BeautifulSoup
import requests
import time

def notifyMe(title, msg):
        notification.notify( title=title, message=msg, app_icon="icon1.ico", timeout=15)

if __name__ == "__main__":

    while(1):
        data = requests.get('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(data.text, "html.parser")
        #tr =soup.find_all("tbody")
        # notifyMe("Alert!!", "check")
        #str=""
        #for x in tr:
        #   str+=x.text
        #print(str)
        #infoList=str.split('\n\n')
        # print(infoList)
        #print(len(infoList))
        #x=len(infoList)
        #storing last row
        #last_row=infoList[x-5:]
        #print(last_row)
        #this will also do [active=soup.select_one("li.bg-blue > strong")]
        active=soup.find("li",{"class":"bg-blue"}).find('strong')
        cure=soup.find("li",{"class":"bg-green"}).find('strong')
        death=soup.find("li",{"class":"bg-red"}).find('strong')
        #print(active.text,cure.text,death.text)
        total=int(active.text)+int(cure.text)+int(death.text)
        #print(total)
        detail="Active cases : {}\nCured : {}\nDeaths : {}\nTotal confirmed cases  : {}".format(active.text,cure.text,death.text,total)
        notifyMe("CORONA'S EFFECT SO FAR IN INDIA", detail)
        time.sleep(30)
