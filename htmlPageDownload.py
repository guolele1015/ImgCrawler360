# -*- coding:utf-8 -*-
import urllib
import os
from bs4 import BeautifulSoup
import json
import shutil
from urllib2 import URLError

def getAKeyFromUser():
    userInputKey = raw_input("请输入一个关键字\n")
    return userInputKey
def getMaxPicNum():
     imgMaxNum = raw_input("请输入要抓取的图片数量\n")
     return imgMaxNum
def getHtmlPage(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getAllImgLink(html,imgPath,keyword):
    soup = BeautifulSoup(html, "lxml")
    jsonStr = soup.p.text
    print "解析后的json串如下:"
    print jsonStr
    # json数据转换
    data = json.loads(jsonStr)
    print data
    for x in range(0,len(data["list"])):
        #下载原图
        print data["list"][x]["img"]
        try:
            urllib.urlretrieve(data["list"][x]["img"], imgPath + "/" + keyword.decode("utf-8").encode("gbk") + "%s.jpg"%x)
        except:
            print "exception"
    return "all files download success"

# Let the user inpur a keyword to search image in "image.so.com"
keyword = getAKeyFromUser()
#judge the folder exist or not
imgPath = "./"+keyword.decode("utf-8").encode("gbk")
confirmFlag = True
isFolderExist = os.path.exists(imgPath)
if isFolderExist:
    choice = raw_input("the path is already exist,do you want to update?")
    if choice == "yes":
        shutil.rmtree(imgPath)
    else:
        userWantUpdate = False
if confirmFlag == True:
    #make a new folder to save all pictures
    os.mkdir(imgPath)
    #get the maxinum number of pictures that user need
    maxPicNum = getMaxPicNum()
    # wraning info
    print "The program will search image in Internet,Please wait...\n"
    linkAdd = "http://image.so.com/j?q="+keyword+"&pn="+maxPicNum
    html = getHtmlPage(linkAdd)
    print getAllImgLink(html,imgPath,keyword)