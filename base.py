
import os  
import requests

#这里是指定本地网络代理 如果没有请注释掉 注释方法 这两行前面加#
os.environ["http_proxy"] = "http://127.0.0.1:7991"
os.environ["https_proxy"] = "http://127.0.0.1:7991"

def saveFile(fileUrlList,fileNameList):
     #print(fileNameList)
     for i in range(len(fileUrlList)):
        url = fileUrlList[i]
        name = fileNameList[i]
        print("downloading Base File "+name)
        r = requests.get(url) 
        with open("base/"+name, "wb") as code:
                code.write(r.content)  
#如果以后多了文件 就按照这个格式直接加一个文件url 和fileName
urls =["https://raw.githubusercontent.com/chaldea-center/chaldea-data/main/dist/wiki.servants.1.json",
       "https://raw.githubusercontent.com/chaldea-center/chaldea-data/main/dist/wiki.servants.2.json",
       "https://raw.githubusercontent.com/chaldea-center/chaldea-data/main/dist/wiki.servants.3.json",
       "https://raw.githubusercontent.com/chaldea-center/chaldea-data/main/dist/wiki.servants.4.json",
       "https://raw.githubusercontent.com/chaldea-center/chaldea-data/main/dist/servants.1.json",
       "https://raw.githubusercontent.com/chaldea-center/chaldea-data/main/dist/servants.2.json",
       "https://raw.githubusercontent.com/chaldea-center/chaldea-data/main/dist/servants.3.json",
       "https://raw.githubusercontent.com/chaldea-center/chaldea-data/main/dist/servants.4.json"]
fileNames = ["wiki.servants.1.json",
             "wiki.servants.2.json",
             "wiki.servants.3.json",
             "wiki.servants.4.json",
             "servants.1.json",
             "servants.2.json",
             "servants.3.json",
             "servants.4.json"]

saveFile(urls,fileNames)