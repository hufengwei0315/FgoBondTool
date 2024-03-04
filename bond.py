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

def sortData(list):
    svtList = []
    for j in range(len(list)):
        svtList.append(SvtData(list[j]["id"], list[j]["svtId"], list[j]["mcLink"],list[j]["bondPoint"],list[j]["bondLevel"],list[j]["bondLeft"],list[j]["treasureDeviceLv1"] ))
    svtList.sort(key=lambda x: x.bondLeft)
    return svtList;

def sortDatalv(list):
    svtList = []
    for j in range(len(list)):
        svtList.append(SvtData(list[j]["id"], list[j]["svtId"], list[j]["mcLink"],list[j]["bondPoint"],list[j]["bondLevel"],list[j]["bondLeft"],list[j]["treasureDeviceLv1"] ))
    svtList.sort(key=lambda x: x.bondLevel)
    return svtList;

def groupData(dataList):
    ltsg = groupby(dataList,key= lambda x:x.bondLevel)
    return ltsg

def data_open_excel(list0,list1,list2,list3,list4,list5):
    title = ['从者id', '从者编号', '名称','羁绊点','羁绊等级','剩余羁绊点']  # 设置表头
    workbook = xw.Workbook('羁绊文件.xlsx') 
    worksheet0 = workbook.add_worksheet("Cost0")
    worksheet1 = workbook.add_worksheet("Cost1")
    worksheet2 = workbook.add_worksheet('Cost2')
    worksheet3 = workbook.add_worksheet('Cost3')
    worksheet4 = workbook.add_worksheet('Cost4')
    worksheet5 = workbook.add_worksheet("Cost5")
    worksheet6 = workbook.add_worksheet("五宝or四宝")

    worksheet5.activate()
    worksheet0.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet2.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet3.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet4.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet5.write_row('A1', title)  # 从A1单元格开始写入表头   
    worksheet6.write_row('A1', title)  # 从A1单元格开始写入表头 
      
    # 五星 cost 16
    i = 2  # 从第二行开始写入数据
    svtList = sortData(list5)
    for j in range(len(svtList)):
        insertData = [svtList[j].id, svtList[j].svtId, svtList[j].mcLink,svtList[j].bondPoint,svtList[j].bondLevel,svtList[j].bondLeft]
        #print(insertData)
        row = 'A' + str(i)
        worksheet5.write_row(row, insertData)
        i += 1
    i = 2  # 从第二行开始写入数据

    for j in range(len(svtList)):
        if ( svtList[j].treasureDeviceLv1 ==5 ):
            insertData = [svtList[j].id, svtList[j].svtId, svtList[j].mcLink,svtList[j].bondPoint,svtList[j].bondLevel,svtList[j].bondLeft]
            #print(svtList[j].treasureDeviceLv1)
            row = 'A' + str(i)
            worksheet6.write_row(row, insertData)
            i += 1
    insertData = ["四宝"]
    row = 'A' + str(i)
    worksheet6.write_row(row, insertData)
    i +=1
    for j in range(len(svtList)):
        if ( svtList[j].treasureDeviceLv1 ==4 ):
            insertData = [svtList[j].id, svtList[j].svtId, svtList[j].mcLink,svtList[j].bondPoint,svtList[j].bondLevel,svtList[j].bondLeft]
            #print(svtList[j].treasureDeviceLv1)
            row = 'A' + str(i)
            worksheet6.write_row(row, insertData)
            i += 1


    # 四星 cost 12
    i = 2  # 从第二行开始写入数据
    svtList = sortData(list4)
    for j in range(len(svtList)):
        insertData = [svtList[j].id, svtList[j].svtId, svtList[j].mcLink,svtList[j].bondPoint,svtList[j].bondLevel,svtList[j].bondLeft]
        #print(insertData)
        row = 'A' + str(i)
        worksheet4.write_row(row, insertData)
        i += 1

    # 三星 cost 7
    i = 2  # 从第二行开始写入数据
    svtList = sortData(list3)
    for j in range(len(svtList)):
        insertData = [svtList[j].id, svtList[j].svtId, svtList[j].mcLink,svtList[j].bondPoint,svtList[j].bondLevel,svtList[j].bondLeft]
        #print(insertData)
        row = 'A' + str(i)
        worksheet3.write_row(row, insertData)
        i += 1

    # 二星 cost 4
    i = 2  # 从第二行开始写入数据
    svtList = sortData(list2)
    for j in range(len(svtList)):
        insertData = [svtList[j].id, svtList[j].svtId, svtList[j].mcLink,svtList[j].bondPoint,svtList[j].bondLevel,svtList[j].bondLeft]
        #print(insertData)
        row = 'A' + str(i)
        worksheet2.write_row(row, insertData)
        i += 1

    # 一星 cost 3
    i = 2  # 从第二行开始写入数据
    svtList = sortData(list1)
    for j in range(len(svtList)):
        insertData = [svtList[j].id, svtList[j].svtId, svtList[j].mcLink,svtList[j].bondPoint,svtList[j].bondLevel,svtList[j].bondLeft]
        #print(insertData)
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1

    #cost 0
    i = 2  # 从第二行开始写入数据
    svtList = sortData(list0)
    for j in range(len(svtList)):
        insertData = [svtList[j].id, svtList[j].svtId, svtList[j].mcLink,svtList[j].bondPoint,svtList[j].bondLevel,svtList[j].bondLeft]
        #print(insertData)
        row = 'A' + str(i)
        worksheet0.write_row(row, insertData)
        i += 1
    workbook.close()
    print('羁绊文件已生成')    


def write_data_to_excel(worksheet,svtList,i):
    dataList = [];
    for j in range(len(svtList)):
        #print(svtList[j].id)
        tinydict ={"id":svtList[j].id,"svtId": svtList[j].svtId,"mcLink":svtList[j].mcLink,"bondPoint":svtList[j].bondPoint,"bondLevel":svtList[j].bondLevel,"bondLeft":svtList[j].bondLeft,"treasureDeviceLv1":svtList[j].treasureDeviceLv1}
        dataList.append(tinydict)

    svtListAfter = sortData(dataList)

    for j in range(len(svtListAfter)):
       insertData = [svtListAfter[j].id, svtListAfter[j].svtId, svtListAfter[j].mcLink,svtListAfter[j].bondPoint,svtListAfter[j].bondLevel,svtListAfter[j].bondLeft]
       #print(insertData)
       row = 'A' + str(i)
       worksheet.write_row(row, insertData)
       i += 1
    return i

def writeGroup(groupLevel,worksheet):
    i = 2  # 从第二行开始写入数据
    for key,group in groupLevel:
       insertData = ["羁绊等级"+str(key)]
       row = 'A' + str(i)
       worksheet.write_row(row, insertData)
       i +=1
       i = write_data_to_excel(worksheet,list(group),i)

def data_open_excel_lv(list0,list1,list2,list3,list4,list5):
    title = ['从者id', '从者编号', '名称','羁绊点','羁绊等级','剩余羁绊点']  # 设置表头
    workbook = xw.Workbook('羁绊等级文件.xlsx') 
    worksheet0 = workbook.add_worksheet("Cost0")
    worksheet1 = workbook.add_worksheet("Cost1")
    worksheet2 = workbook.add_worksheet('Cost2')
    worksheet3 = workbook.add_worksheet('Cost3')
    worksheet4 = workbook.add_worksheet('Cost4')
    worksheet5 = workbook.add_worksheet("Cost5")
    worksheet5.activate()
    worksheet0.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet2.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet3.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet4.write_row('A1', title)  # 从A1单元格开始写入表头
    worksheet5.write_row('A1', title)  # 从A1单元格开始写入表头        
    # 五星 cost 16
    svtList = sortDatalv(list5)
    groupLevel = groupData(svtList) 
    writeGroup(groupLevel,worksheet5)
    # 四星 cost 12    
    svtList = sortDatalv(list4)
    groupLevel = groupData(svtList) 
    writeGroup(groupLevel,worksheet4)

    # 三星 cost 7
    svtList = sortDatalv(list3)
    groupLevel = groupData(svtList) 
    writeGroup(groupLevel,worksheet3)

    # 二星 cost 4
    svtList = sortDatalv(list2)
    groupLevel = groupData(svtList) 
    writeGroup(groupLevel,worksheet2)

    # 一星 cost 3
    svtList = sortDatalv(list1)    
    groupLevel = groupData(svtList) 
    writeGroup(groupLevel,worksheet1)

    #cost 0
    svtList = sortDatalv(list0)
    groupLevel = groupData(svtList) 
    writeGroup(groupLevel,worksheet0)

    workbook.close()
    print('羁绊文件已生成')    

if(os.path.exists("羁绊文件.xlsx")):
    print('羁绊过期文件已删除')
    os.remove("羁绊文件.xlsx")
if(os.path.exists("羁绊等级文件.xlsx")):
    print('羁绊等级过期文件已删除')
    os.remove("羁绊等级文件.xlsx")

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
collection = user_dic['cache']['replaced']['userSvtCollection']
#print(collection)
#print (type(collection))

list0 = [];
list1 = [];
list2 = [];
list3 = [];
list4 = [];
list5 = [];
for key in range (len(collection)):
    bond_point_level = int(collection[key]['friendshipRank'])
    point  = int (collection[key]['friendship'])
    point_str = collection[key]['friendship']
    svt_id = int(collection[key]['svtId'])
    treasureDeviceLv1 = int(collection[key]['treasureDeviceLv1'])
    if ( bond_point_level >= 0):
      #print (collection[key]['svtId'] +':'+point_str)
      #print(bond_point_level)
      for key2 in range (len(svt_data)):
        idX = svt_data[key2]['idX']
        status = int(collection[key]['status'])
        if(idX == svt_id and status == 2):
           bond_list = svt_data[key2]['servantBondGrowthList']
           for key3 in range (len (bond_list)):
            svt_bond_level = int(bond_list[key3]['level']) - 1
            if(svt_bond_level == bond_point_level):
                left_value = bond_list[key3]['bondPoint'] - point
                #print('svt'+svt_data[key2]['mcLink'] +' id:'+str(idX) +' left point:'+str(left_value) + ' bond_level:' + str(bond_point_level))
                if(svt_data[key2]['cost']==16):
                    # [data[j]["id"], data[j]["svtId"], data[j]["mcLink"],data[j]["bondPoint"],data[j]["bondLevel"],data[j]["bondLeft"]]
                    tinydict ={"id":idX,"svtId":svt_data[key2]['collectionNo'],"mcLink":svt_data[key2]['mcLink'],"bondPoint":point,"bondLevel":svt_bond_level,"bondLeft":left_value,"treasureDeviceLv1":treasureDeviceLv1}
                    list5.append(tinydict)
                if(svt_data[key2]['cost']==12):
                    # [data[j]["id"], data[j]["svtId"], data[j]["mcLink"],data[j]["bondPoint"],data[j]["bondLevel"],data[j]["bondLeft"]]
                    tinydict ={"id":idX,"svtId":svt_data[key2]['collectionNo'],"mcLink":svt_data[key2]['mcLink'],"bondPoint":point,"bondLevel":svt_bond_level,"bondLeft":left_value,"treasureDeviceLv1":treasureDeviceLv1}
                    list4.append(tinydict)
                if(svt_data[key2]['cost']==7):
                    # [data[j]["id"], data[j]["svtId"], data[j]["mcLink"],data[j]["bondPoint"],data[j]["bondLevel"],data[j]["bondLeft"]]
                    tinydict ={"id":idX,"svtId":svt_data[key2]['collectionNo'],"mcLink":svt_data[key2]['mcLink'],"bondPoint":point,"bondLevel":svt_bond_level,"bondLeft":left_value,"treasureDeviceLv1":treasureDeviceLv1}
                    list3.append(tinydict)
                if(svt_data[key2]['cost']==4):
                    # [data[j]["id"], data[j]["svtId"], data[j]["mcLink"],data[j]["bondPoint"],data[j]["bondLevel"],data[j]["bondLeft"]]
                    tinydict ={"id":idX,"svtId":svt_data[key2]['collectionNo'],"mcLink":svt_data[key2]['mcLink'],"bondPoint":point,"bondLevel":svt_bond_level,"bondLeft":left_value,"treasureDeviceLv1":treasureDeviceLv1}
                    list2.append(tinydict)
                if(svt_data[key2]['cost']==3):
                    # [data[j]["id"], data[j]["svtId"], data[j]["mcLink"],data[j]["bondPoint"],data[j]["bondLevel"],data[j]["bondLeft"]]
                    tinydict ={"id":idX,"svtId":svt_data[key2]['collectionNo'],"mcLink":svt_data[key2]['mcLink'],"bondPoint":point,"bondLevel":svt_bond_level,"bondLeft":left_value,"treasureDeviceLv1":treasureDeviceLv1}
                    list1.append(tinydict)
                if(svt_data[key2]['cost']==0):
                    # [data[j]["id"], data[j]["svtId"], data[j]["mcLink"],data[j]["bondPoint"],data[j]["bondLevel"],data[j]["bondLeft"]]
                    tinydict ={"id":idX,"svtId":svt_data[key2]['collectionNo'],"mcLink":svt_data[key2]['mcLink'],"bondPoint":point,"bondLevel":svt_bond_level,"bondLeft":left_value,"treasureDeviceLv1":treasureDeviceLv1}
                    list0.append(tinydict)



data_open_excel(list0,list1,list2,list3,list4,list5)
data_open_excel_lv(list0,list1,list2,list3,list4,list5) 
