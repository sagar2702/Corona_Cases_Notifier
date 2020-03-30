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
        tr =soup.find_all("tbody")
        # notifyMe("Alert!!", "check")
        str=""
        for x in tr:
            str+=x.text
        #print(str)
        infoList=str.split('\n\n')
        #print(infoList)
        #print(len(infoList))
        x=len(infoList)
        #storing last row
        #last_row=infoList[x-5:x-1]
        last_row=infoList[x-4:x-1]
        #print(last_row)
        last_row_col_1=last_row[0].split('\n')[2]
        last_row_col_2=last_row[1].split('\n')[1]
        last_row_col_3 = last_row[2].split('\n')[1]
        #last_row_col_4 = last_row[3].split('\n')[1]
        #print(last_row_col_1,last_row_col_2, last_row_col_3, last_row_col_4)
        #detail="Indian confirmed cases  : {}\nForeigner confirmed cases: {}\nCured : {}\nDeath : {}".format(last_row_col_1,last_row_col_2,last_row_col_3,last_row_col_4)
        detail="Total confirmed cases  : {}\nCured : {}\nDeath : {}".format(last_row_col_1,last_row_col_2,last_row_col_3)

        notifyMe("CORONA'S EFFECT SO FAR IN INDIA", detail)
        time.sleep(30)
