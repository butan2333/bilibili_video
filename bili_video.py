import bili_author
class bili_video:
    def __init__(self,url='',author=bili_author(),name='',intro='',playTimes=0,barrageNum=0,coverUrl=''):
        self.author=author
        self.url=url
        self.name=name
        self.intro=intro
        self.playTimes=playTimes
        self.barrageNum=barrageNum
        self.coverUrl=coverUrl
        self.author.addVideo(self)
    
    def getAuthor(self):
        return self.author

    def getUrl(self):
        return self.url
        
    def getName(self):
        return self.name

    def getIntro(self):
        return self.intro

    def getPlayTimes(self):
        return self.playTimes

    def getBarrageNum(self):
        return self.playTimes

    def getCoverUrl(self):
        return self.coverUrl
    def setAuthor(self,author):
        self.author=author
        self.author.addVideo(self)