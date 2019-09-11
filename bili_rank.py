from pymongo import MongoClient
from pymongo import ASCENDING
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
class bili_rank:
    def __init__(self):
        self.dict_danmaku={}
        self.dict_view={}
        self.dict_favorite={}
        self.dict_share={}
        self.dict_like={}
        self.dict_coin={}

    def connectMongoDB(self,adress='127.0.0.1',port=27017):
        self.client=MongoClient(adress,port)
        self.db=self.client['bilibili']
        self.rank()
    
    def rank(self):
        coll_names = self.db.list_collection_names(session=None)
        for i in coll_names:
            coll=self.db[i]
            results = coll.find().sort('owner',ASCENDING)
            
            r=0
            for result in results:
                if result['owner']['name']!=r:
                    r=result['owner']['name']
                    self.dict_danmaku[r]=result['stat']['danmaku'] 
                    self.dict_view[r]=result['stat']['view'] 
                    self.dict_favorite[r]=result['stat']['favorite'] 
                    self.dict_share[r]=result['stat']['share'] 
                    self.dict_like[r]=result['stat']['like'] 
                    self.dict_coin[r]=result['stat']['coin'] 
                else:
                    self.dict_danmaku[result['owner']['name']]+=result['stat']['danmaku']
                    self.dict_view[result['owner']['name']]+=result['stat']['view'] 
                    self.dict_favorite[result['owner']['name']]+=result['stat']['favorite'] 
                    self.dict_share[result['owner']['name']]+=result['stat']['share'] 
                    self.dict_like[result['owner']['name']]+=result['stat']['like'] 
                    self.dict_coin[result['owner']['name']]+=result['stat']['coin'] 

    def getRanking(self,type_to_dispaly):
        num_to_dispaly=int(input('请输入你想查看的排行数：'))
        if type_to_dispaly!=0:
            switcher1={
                1:self.dict_view,
                2:self.dict_like,
                3:self.dict_favorite,
                4:self.dict_share,
                5:self.dict_coin,
                6:self.dict_danmaku,
            }
            
            sorted_dict_r=sorted(switcher1.get(type_to_dispaly).items(),key=lambda item:item[1],reverse=True)
            name=[]
            fav_num=[]
            for i in range(num_to_dispaly):
                name.append(sorted_dict_r[i][0])
                fav_num.append(sorted_dict_r[i][1])
            plt.barh(range(len(fav_num)), list(reversed(fav_num)),tick_label = list(reversed(name))) 
            plt.show()
        else:
            
            '''
            
            danmuku_num=[]
            view_num=[]
            fav_num=[]
            share_num=[]
            like_num=[]
            coin_num=[]
            '''
            name=[]
            num_list=[]
            for i in range(6):
                num_list.append([])
            sorted_dict_r=sorted(self.dict_danmaku.items(),key=lambda item:item[1],reverse=True)
            for i in range(num_to_dispaly):
                name.append(sorted_dict_r[i][0])
                num_list[0].append(self.dict_danmaku[sorted_dict_r[i][0]])
                num_list[1].append(self.dict_view[sorted_dict_r[i][0]])
                num_list[2].append(self.dict_favorite[sorted_dict_r[i][0]])
                num_list[3].append(self.dict_share[sorted_dict_r[i][0]])
                num_list[4].append(self.dict_like[sorted_dict_r[i][0]])
                num_list[5].append(self.dict_coin[sorted_dict_r[i][0]])
            total_height, n = 0.8, 2
            height = total_height / n
            type_name=['弹幕数','浏览数','收藏数','分享数','点赞数','硬币数']
            for i in range(len(num_list)-1):
                plt.barh(range(len(num_list[i])),list(reversed(num_list[i])),height=height,label=type_name[i])
            plt.barh(range(len(num_list[5])),list(reversed(num_list[5])),height=height,label=type_name[5],tick_label = list(reversed(name)))
            plt.legend()
            plt.show()
            


bilirank=bili_rank()
bilirank.connectMongoDB()
while True:
    try:
        in_type=input("输入你想查看的排行类型(输入q退出)：\n0. 全部排行 \n1. 浏览数排行\n2. 点赞数排行\n3. 收藏数排行\n4. 分享数排行\n5. 硬币数排行\n6. 弹幕数排行\n")
        if in_type!='q':
            bilirank.getRanking(int(in_type))
        else:
            break
    except Exception as e:
        print(e)