#  pip3 install xlsxwriter
import json
import os
import xlsxwriter as xw
from itertools import groupby
import requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from io import BytesIO

class SvtData:
    def __init__(self,id,svtId,mcLink,bondPoint,bondLevel,bondLeft,treasureDeviceLv1):
        self.id = id
        self.svtId = svtId
        self.mcLink = mcLink
        self.bondPoint = bondPoint
        self.bondLevel= bondLevel
        self.bondLeft = bondLeft
        self.treasureDeviceLv1 = treasureDeviceLv1
class itemData:
    def __init__(self,itemName,itemId,count,url):
        self.itemName = itemName
        self.itemId = itemId
        self.count= count
        self.url = url

def sortData(list):
    svtList = []
    for j in range(len(list)):
        svtList.append(itemData(list[j]["itemName"], list[j]["itemId"], list[j]["count"],list[j]["url"]))
    svtList.sort(key=lambda x: x.count)
    return svtList;


os.environ["http_proxy"] = "http://127.0.0.1:7991"
os.environ["https_proxy"] = "http://127.0.0.1:7991"
file_name  = "bond_servant.json"
object = open(file_name,encoding="utf-8")
try:
    all_the_text = object.read()  #结果为str类型
    svt_data = json.loads(all_the_text);
finally:
    object.close()

user_data_path = "result.json" 
user_file_object = open(user_data_path,encoding="utf-8")
try:
    user_data_text = user_file_object.read()  #结果为str类型
finally:
    user_file_object.close()

servant_data_path = "base/servants.json"
servant_data_object = open(servant_data_path,encoding="utf-8")
try:
    servant_data_text = servant_data_object.read()  #结果为str类型
finally:
    servant_data_object.close()


item_data_path="bond_item.json"
item_data_object = open(item_data_path,encoding="utf-8")
try:
    item_data_text = item_data_object.read()  #结果为str类型
finally:
    item_data_object.close()


user_dic = json.loads(user_data_text)
collection = user_dic['cache']['replaced']['userSvt']
#print(collection)
#print (type(collection))
servant_dic = json.loads(servant_data_text)
item_idc= json.loads(item_data_text)

list0 = [];

collection2 = user_dic['cache']['replaced']['userSvtAppendPassiveSkill']
#print(len(collection2))

collection3 = user_dic['cache']['replaced']['userSvtAppendPassiveSkillLv']
user_item =  user_dic['cache']['replaced']['userItem']
#print(len(collection3))


def download_image(url):
    """下载图片并返回图片的二进制数据"""
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    return BytesIO(response.content)
def insert_excel(list0):
    if(os.path.exists("素材详情.xlsx")):
        print('素材详情已删除')
        os.remove("素材详情.xlsx")

    title = ['id', '名称', '素材','数量','素材id']  # 设置表头
    workbook = xw.Workbook('素材详情.xlsx') 
    worksheet0 = workbook.add_worksheet("sheet1")
    worksheet0.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(list0)):
        #print(list1[j])
        insertData = [list0[j]['svtId'], list0[j]['mclink'], list0[j]['itemName'],list0[j]['count'],list0[j]['itemId']]
        #print(insertData)
        row = 'A' + str(i)
        worksheet0.write_row(row, insertData)
        i += 1
    workbook.close()

def insert_total_excel(list0):
    if(os.path.exists("素材总需求.xlsx")):
        print('素材总需求已删除')
        os.remove("素材总需求.xlsx")

    title = ['图片','素材','数量','素材id']  # 设置表头
    workbook = xw.Workbook('素材总需求.xlsx') 
    worksheet0 = workbook.add_worksheet("sheet1")
    worksheet0.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    itemList = sortData(list0)
    for j in range(len(itemList)):
        worksheet0.set_row(i-1,30)
        #print(list1[j])
        image_path = 'base/item/'+itemList[j].itemName+'.jpg'
        try:
            if os.path.exists(image_path):
                 worksheet0.insert_image(i-1,0,image_path,
                                    {
                                     "x_scale": 0.25,
                                    "y_scale": 0.25})
            else:
                print("正在下载...."+itemList[j].url)
                image_data = download_image(itemList[j].url)
                print("下载完成！ "+itemList[j].itemName)
                worksheet0.insert_image(i-1,0,f"image_{j+1}.png",
                                    {"image_data":image_data,
                                     "x_scale": 0.25,
                                    "y_scale": 0.25})
        except Exception as e:
            worksheet0.write(i-1, 4, f"Error: {e}") 
        insertData = [ itemList[j].itemName,itemList[j].count,itemList[j].itemId]
        #print(insertData)
        row = 'B' + str(i)
        worksheet0.write_row(row, insertData)    
        i += 1
    workbook.close()

for key in range (len(collection)):
    id = int(collection[key]['id'])
    svt_id = int(collection[key]['svtId'])
    skillLv1 = (int)(collection[key]['skillLv1'])
    skillLv2 = (int)(collection[key]['skillLv2'])
    skillLv3 = (int)(collection[key]['skillLv3'])
    appendSkillLv2=1
    appendSkillLv5=1
    mclink = ""
    for key2 in range (len(collection3)):
        userSvtId = collection3[key2]['userSvtId']
   
        if((int)(userSvtId) == id):
            appendPassiveSkillLvs = collection3[key2]['appendPassiveSkillLvs']
            appendPassiveSkillNums = collection3[key2]['appendPassiveSkillNums']
            for num in range(len(appendPassiveSkillNums)):
                sequence = appendPassiveSkillNums[num]
                if sequence == 101:
                    appendSkillLv2 =(int) (appendPassiveSkillLvs[num])
                if sequence == 104:
                    appendSkillLv5 = (int)(appendPassiveSkillLvs[num])
            #input("Press Enter to continue...")
                
    for n in range (len(svt_data)):
     idX = svt_data[n]['idX']
     status = int(collection[key]['status'])
     if(idX == svt_id ):
     #if(idX == svt_id ):
      mclink = svt_data[n]['mcLink']
      cost = svt_data[n]['cost']
      if mclink != "" and cost >=12 :
        #print(mclink+"   " +"\n skill1 "+str(skillLv1)+" skill2 "+str(skillLv2)+" skill3 "+str(skillLv3)+"\n appendskill2 "+str(appendSkillLv2)+" appendskill5 "+str(appendSkillLv5))
        tinydict ={"id":idX,"svtId":svt_data[n]['collectionNo'],"mcLink":svt_data[n]['mcLink'],"appendFlag":False,"skillLv":skillLv1}
        list0.append(tinydict)
        tinydict ={"id":idX,"svtId":svt_data[n]['collectionNo'],"mcLink":svt_data[n]['mcLink'],"appendFlag":False,"skillLv":skillLv2}
        list0.append(tinydict)
        tinydict ={"id":idX,"svtId":svt_data[n]['collectionNo'],"mcLink":svt_data[n]['mcLink'],"appendFlag":False,"skillLv":skillLv3}
        list0.append(tinydict)
        tinydict ={"id":idX,"svtId":svt_data[n]['collectionNo'],"mcLink":svt_data[n]['mcLink'],"appendFlag":True,"skillLv":appendSkillLv2}
        list0.append(tinydict)
        tinydict ={"id":idX,"svtId":svt_data[n]['collectionNo'],"mcLink":svt_data[n]['mcLink'],"appendFlag":True,"skillLv":appendSkillLv5}
        list0.append(tinydict)
#print(list0)
result = []
for index in range(len(list0)):
    svtId = list0[index]['id']
    level =(int) (list0[index]['skillLv'])
    appendFlag = list0[index]['appendFlag']
    
    #print(svtId)
    for key2 in range(len (servant_dic)):
        id = servant_dic[key2]['id']
        #input("Press Enter to continue...")
        if (id == svtId ):
            #input("Press Enter to continue...")
            if( appendFlag == False):
                skillMaterials = servant_dic[key2]['skillMaterials']
            else:
                skillMaterials = servant_dic[key2]['appendSkillMaterials']
         
            if level != 10:
                for tempLevel in range (len(skillMaterials)):
                    if tempLevel+1 > level :
                        levelItemList = skillMaterials[str(tempLevel)]
                        for j in range(len(levelItemList['items'])):
                            item = levelItemList['items'][j]
                            itemId = str(item['itemId'])
                            count = int(item['amount'])
                            for k in range(len(item_idc)) :
                                if int(item_idc[k]['id']) == int(itemId):
                                    #print(str(svtId)+" "+list0[index]['mcLink']+" "+str(item_idc[k]['name'])+" "+str(item['amount']))
                                    result_dict = {"svtId":svtId,'mclink':list0[index]['mcLink'],"level":tempLevel,"itemName":str(item_idc[k]['name']),"itemId":itemId,"count":count,"url":item_idc[k]['icon']}  
                                    result.append(result_dict)

#print(result)

insert_excel(result)

total_result = []
for j in range(len(result)):
    itemId= int(result[j]['itemId'])
    count = int(result[j]['count'])
    itemName = result[j]['itemName']
    url = result[j]['url']
    exist_flag = False
    k = -1
    for index in range(len(total_result)):
        if total_result[index]['itemId'] == itemId:
            exist_flag = True
            k = index
    
    if exist_flag:
        total_amount = int(total_result[k]['count']) + int (result[j]['count'])
        total_result[k]['count'] = total_amount
    else :
        result_dict = {"itemName":itemName,"itemId":itemId,"count":count,"url":url}  
        total_result.append(result_dict)
for j in range(len(total_result)):
    result_item  = total_result[j]
    for index in range(len(user_item)):
        item_id = user_item[index]['itemId']
        if int(item_id) == int(result_item['itemId']):
            total_amount =    int (user_item[index]['num']) - int(total_result[j]['count'])
            total_result[j]['count'] = total_amount

insert_total_excel(total_result)