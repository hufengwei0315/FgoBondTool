import json
import os

#合并文件函数
def open_base_file(base_files,after_name):
    allData = list()
    for i in range(len(base_files)):
        file_name = base_files[i]
        object = open('base/'+file_name,encoding="utf-8")
        try:
            all_the_text = object.read()  #结果为str类型
            svt_data = json.loads(all_the_text);
            allData.extend(svt_data);
        finally:
            object.close()
    print("Saving File:"+after_name)
    #print(allData)
    with open('base/'+after_name, 'w',encoding='utf-8') as f:
      json.dump(allData,f,ensure_ascii=False)

fileNames =  ["wiki.servants.1.json",
             "wiki.servants.2.json",
             "wiki.servants.3.json",
             "wiki.servants.4.json",
             "wiki.servants.5.json",]
baseFiles =[ "servants.1.json",
             "servants.2.json",
             "servants.3.json",
             "servants.4.json",
             "servants.5.json"]

#json 文件合并
open_base_file(baseFiles,"servants.json")
open_base_file(fileNames,"wiki.servants.json")

file_name  = 'base/'+"servants.json"
object = open(file_name,encoding="utf-8")
try:
    all_the_text = object.read()  #结果为str类型
    base_data = json.loads(all_the_text);
finally:
    object.close()

user_data_path =  'base/'+"wiki.servants.json" 
user_file_object = open(user_data_path,encoding="utf-8")

try:
    user_data_text = user_file_object.read()  #结果为str类型
finally:
    object.close()
wiki_data = json.loads(user_data_text)

bond_servant = []
for key in range (len(base_data)):
    collection_no = int( base_data[key]['collectionNo'])
    id = base_data[key]['id']
    cost = base_data[key]['cost']
    bond_growth = base_data[key]['bondGrowth']
    mcLink = ''
    for j in range(len(wiki_data)):
        if  int(wiki_data[j]['collectionNo']) == collection_no:
            mcLink = wiki_data[j]['mcLink']
    #print(collection_no,":",id,":",cost,":",mcLink)

    servant_bond_growthList = [];
    for j in range (len(bond_growth)):
        num = j+1
        tiny_dict = {"bondPoint":bond_growth[j],"level":num}
        servant_bond_growthList.append(tiny_dict)
    #print(servant_bond_growthList)
    item_dict = {"idX":id,"collectionNo":collection_no,"cost":cost,"mcLink":mcLink,"servantBondGrowthList":servant_bond_growthList}
    bond_servant.append(item_dict)


with open('bond_servant.json', 'w',encoding='utf-8') as f:
    json.dump(bond_servant,f,ensure_ascii=False)