
import os  
import requests
import json
from io import BytesIO
from PIL import Image

#这里是指定本地网络代理 如果没有请注释掉 注释方法 这两行前面加#
os.environ["http_proxy"] = "http://127.0.0.1:7991"
os.environ["https_proxy"] = "http://127.0.0.1:7991"

def download_image(url):
    """下载图片并返回图片的二进制数据"""
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    return BytesIO(response.content)

# https://raw.githubusercontent.com/chaldea-center/chaldea-data/refs/heads/main/dist/items.json
# https://raw.githubusercontent.com/chaldea-center/chaldea-data/refs/heads/main/mappings/item_names.json
def saveFile(fileUrlList,fileNameList):
     #print(fileNameList)
     for i in range(len(fileUrlList)):
        url = fileUrlList[i]
        name = fileNameList[i]
        print("downloading Base File "+name)
        r = requests.get(url) 
        with open("base/item/"+name, "wb") as code:
                code.write(r.content)  
#如果以后多了文件 就按照这个格式直接加一个文件url 和fileName
urls =["https://raw.githubusercontent.com/chaldea-center/chaldea-data/refs/heads/main/dist/items.json",
       "https://raw.githubusercontent.com/chaldea-center/chaldea-data/refs/heads/main/mappings/item_names.json"]
fileNames = ["item.json",
             "item_names.json",]

saveFile(urls,fileNames)

file_name  = 'base/item/'+"item.json"
object = open(file_name,encoding="utf-8")
try:
    all_the_text = object.read()  #结果为str类型
    base_data = json.loads(all_the_text);
finally:
    object.close()

user_data_path =  'base/item/'+"item_names.json" 
user_file_object = open(user_data_path,encoding="utf-8")

try:
    user_data_text = user_file_object.read()  #结果为str类型
finally:
    object.close()
wiki_data = json.loads(user_data_text)

bond_item = []



for key in range (len(base_data)):
    collection_no = int( base_data[key]['id'])
    oldName = base_data[key]['name']
    itemNames = wiki_data[oldName]
    #print(oldName)
    #print(type(itemNames))
    #print(itemNames)
    #print(itemNames["CN"])
    item_dict={"id":collection_no,"name":itemNames["CN"],"icon":base_data[key]['icon']}
    bond_item.append(item_dict)
    try:
        image = Image.open((download_image(item_dict['icon'])))
        rgb_im = image.convert('RGB')
        rgb_im.save('base/item/'+item_dict['name']+'.jpg')
        print(item_dict['name']+'.jpg'+'图片下载保存完成')
    except Exception as e:
        print(item_dict['name']+'.jpg'+'图片下载保存失败')


with open('bond_item.json', 'w',encoding='utf-8') as f:
    json.dump(bond_item,f,ensure_ascii=False)

