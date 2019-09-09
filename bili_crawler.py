from pymongo import MongoClient
import requests
import json 
from lxml import etree

class bili_crawer:
    def getList(self,url):
        r=requests.get(url)
        js=json.loads(r.content)
        try:
            if(len(js['data']['archives'])==0):
                return False
            for i in js['data']['archives']:
                self.db[i['tname']].insert(i)
        except Exception as e:
            print(e)
            
        return True     

    #音乐区 28:32
    def getAllList(self,channelList=[str(i) for i in range(19,34)]):
        
        for i in channelList:
            j=0
            while True:
                j+=1
                url='https://api.bilibili.com/x/web-interface/newlist?rid='+i+'&type=0&pn='+str(j)+'&ps=100'
                if not self.getList(url):
                    break
                print(j)


    
    def connectMongoDB(self,adress='127.0.0.1',port=27017):
        self.client=MongoClient(adress,port)
        self.db=self.client['bilibili']

biliaudio=bili_crawer()
biliaudio.connectMongoDB()
biliaudio.getAllList(['30','31'])
