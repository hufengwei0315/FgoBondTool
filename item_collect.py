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
    def __init__(self,id,svtId,mcLink,skillLv):
        self.id = id
        self.svtId = svtId
        self.mcLink = mcLink
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

user_dic = json.loads(user_data_text)
collection = user_dic['cache']['replaced']['userSvt']
#print(collection)
#print (type(collection))

list0 = [];
list1 = [];
list2 = [];
list3 = [];
list4 = [];
list5 = [];

collection2 = user_dic['cache']['replaced']['userSvtAppendPassiveSkill']
print(len(collection2))

collection3 = user_dic['cache']['replaced']['userSvtAppendPassiveSkillLv']
print(len(collection3))


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
      cost = svt_data[key2]['cost']
      if mclink != "" and cost >=12 :
          print(mclink+"   "+ str(id) +"\n skill1 "+str(skillLv1)+" skill2 "+str(skillLv2)+" skill3 "+str(skillLv3)+"\n appendskill2 "+str(appendSkillLv2)+" appendskill5 "+str(appendSkillLv5))
      





