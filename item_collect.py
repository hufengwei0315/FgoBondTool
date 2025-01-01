#  pip3 install xlsxwriter
import json
import os
import xlsxwriter as xw
from itertools import groupby

class SvtData:
    def __init__(self,id,svtId,mcLink,bondPoint,bondLevel,bondLeft,treasureDeviceLv1):
        self.id = id
        self.svtId = svtId
        self.mcLink = mcLink
        self.bondPoint = bondPoint
        self.bondLevel= bondLevel
        self.bondLeft = bondLeft
        self.treasureDeviceLv1 = treasureDeviceLv1
class SvtData:
    def __init__(self,id,svtId,mcLink,appendFlag,skillLv):
        self.id = id
        self.svtId = svtId
        self.mcLink = mcLink
        self.appendFlag = appendFlag
        self.skillLv= skillLv





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
    object.close()

servant_data_path = "base/servants.json"
servant_data_object = open(servant_data_path,encoding="utf-8")

try:
    servant_data_text = servant_data_object.read()  #结果为str类型
finally:
    object.close()

user_dic = json.loads(user_data_text)
collection = user_dic['cache']['replaced']['userSvt']
#print(collection)
#print (type(collection))
servant_dic = json.loads(servant_data_text)


list0 = [];

collection2 = user_dic['cache']['replaced']['userSvtAppendPassiveSkill']
#print(len(collection2))

collection3 = user_dic['cache']['replaced']['userSvtAppendPassiveSkillLv']
#print(len(collection3))


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
            #print(appendPassiveSkillLvs)
            #print(appendPassiveSkillNums)
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
for index in range(len(list0)):
    svtId = list0[index]['id']
    level =(int) (list0[index]['skillLv'])
    appendFlag = list0[index]['appendFlag']
    #print(svtId)
    for key2 in range(len (servant_dic)):
        id = servant_dic[key2]['id']
        #print(id+" "+svtId)
        #print(id)
        #input("Press Enter to continue...")
        if (id == svtId ):
            #print(int(id)+" "+svtId)
            #input("Press Enter to continue...")
            if( appendFlag == True):
                skillMaterials = servant_dic[key2]['skillMaterials']
            else:
                 skillMaterials = servant_dic[key2]['appendSkillMaterials']
         
            if level != 10:
                for tempLevel in range (len(skillMaterials)-1):
                    #print(skillMaterials['1'])
                    #print(tempLevel)
                    #print(level)
                    if tempLevel+1 > level :
                        levelItemList = skillMaterials[str(tempLevel)]
                        print(levelItemList)
                        for j in range(len(levelItemList['items'])):
                            item = levelItemList['items'][j]
                            print(str(svtId)+" "+str(item['itemId'])+" "+str(item['amount']))
                            #print(str(item['amount']))
                    