# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import numpy as np
import time
from bottle import template
import requests
import csv
import os


def lotto():  
    r = requests.get("https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx")
    soup = BeautifulSoup(r.text,"lxml")
    soup_no=[]      
    for i in range(0,7):    
        for j in range(1,7):             
            savage = "Lotto649Control_history_dlQuery_SNo"+str(j)+"_"+str(i)            
            sub_list = savage[0:]
            list_result = soup.find(id=sub_list).string
            soup_no.append(list_result)               
    return soup_no[0:]
            
if __name__ == '__main__':
    TEMPLATE = "./樂透爬蟲 寫入html/template.html"
    INDEX_HTML = "./樂透爬蟲 寫入html/index.html"

    

    with open(INDEX_HTML, 'wb') as f:        
        lottolist=lotto()    
        #lottostr = "\n".join('%s' %id for id in lottolist)
        for seq in  range(0,len(lottolist),6):
            
            store_lotto=lottolist[seq:seq+6]
            html = template(TEMPLATE, items=store_lotto , seq = int((seq/6)+1))  
            f.write(html.encode("utf-8"))     
       # breakpoint()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("=======success========")
        f.close()     

       
