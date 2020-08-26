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
    lotto_item=[]  
    seq_keep = []               
    for seq in range(0,len(soup_no),6):                     
        store_lotto = soup_no[seq:seq+6]             
        lotto_item.append(store_lotto)  
        seq_keep.append(seq)             
    return lotto_item,seq_keep
            
if __name__ == '__main__':
    TEMPLATE = "./template.html"
    INDEX_HTML = "./index.html"
    lotto_function = lotto()
    lotto_item = lotto_function[0]
    seq_keep = lotto_function[1]
    print(lotto_item)
    with open(INDEX_HTML, 'wb') as f:
        html = template(TEMPLATE, items=lotto_item)  
        f.write(html.encode("utf-8"))     
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("=======success========")
        f.close()     

       
