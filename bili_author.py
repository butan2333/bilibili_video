import bili_video as bv
class bili_author:
    def __init__(self,uid='',avator='',name=''):
        self.uid=uid
        self.avator=avator
        self.name=name
        self.videoList=[]
    
    def getUid(self):
        return self.uid
    
    def getAvator(self):
        return self.avator
    
    def getName(self):
        return self.name
    def addVideo(self,bv):
        self.videoList.append(bv)