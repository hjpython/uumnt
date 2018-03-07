#!/usr/bin/env python
# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import os
import urllib.error
import shutil
import re
from config import dir

def xiazai_uumnt(url):
    html = urllib.request.urlopen(url).read()
    title0 = BeautifulSoup(html,'lxml').find("div",{"class":"bg-white p15 center imgac clearfix"}).find("h1",{"class":"center"}).get_text()
    pattern = re.compile(".*\(")
    title = pattern.findall(title0)
    title = title[0]
    title = title[:-1]
    print(title)
    page = title0[-6:]
    pattern = re.compile("\/\d*")
    page = pattern.findall(page)[0]
    pattern = re.compile("\d*")
    page = pattern.findall(page)[1]
    print("共"+page+"页")
    try:
        os.makedirs(dir + title + '_' + page)
    except:
        shutil.rmtree(dir + title + '_' + page)
        os.makedirs(dir + title + '_' + page)
    html = urllib.request.urlopen(url).read()
    picurl = BeautifulSoup(html,'lxml').find("div",{"class": "bg-white p15 center imgac clearfix"}).find("img")["src"]
    print(picurl)
    img = urllib.request.urlopen(picurl).read()
    f = open(dir + title + '_' + page + "\\" + "1.jpg", "wb")
    f.write(img)
    f.close()
    after = int(page) + 1
    for i in range(2, after):
        try:
            url0 = url[:-5]
            url1 = url0 + '_' + str(i) + '.html'
            html = urllib.request.urlopen(url1).read()
            picurl = BeautifulSoup(html,'lxml').find("div", {"class": "bg-white p15 center imgac clearfix"}).find("img")["src"]
            print(picurl)
            img = urllib.request.urlopen(picurl).read()
            f = open(dir + title + '_' + page + "\\" + str(i) + ".jpg", "wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
                continue
            elif hasattr(e, "reason"):
                print(e.reason)
                continue

if __name__ == '__main__':
    while True:
        url = input("请输入网址:")
        xiazai_uumnt(url)
