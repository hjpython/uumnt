import urllib.request
import pymysql,os,re,shutil
from bs4 import BeautifulSoup
import urllib.error
from config import dir,kw

def req_add(picurl):
    req = urllib.request.Request(picurl)
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
    req.add_header("Accept-Encoding", "gzip,deflate")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.9")
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.25 Safari/537.36")
    req.add_header("Cookie",
                   "bdshare_firstime=1514538484412; UM_distinctid=160a187435124-03f316a3ae33c8-5d4e231d-144000-160a1874352a87; CNZZDATA3866066=cnzz_eid%3D935699110-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1514538490,1514565948; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1514567510")
    req.add_header("Referer", "http://www.mm131.com/xinggan/3561.html")
    req.add_header("Connection", "keep-alive")
    req.add_header("Host", "img1.mm131.me")
    return req

def sql(url):
    conn = pymysql.connect(**kw)
    cur = conn.cursor()
    sql = ("insert into uumnt(url)" "values(%s)")
    cur.execute(sql, url)
    conn.commit()
    cur.close()
    conn.close()

def sqll(url):
    conn = pymysql.connect(**kw)
    cur = conn.cursor()
    sql = ("insert into uumntu(url)" "values(%s)")
    cur.execute(sql, url)
    conn.commit()
    cur.close()
    conn.close()

def xiazai_uumnt(url):
    html = urllib.request.urlopen(url).read()
    title0 = BeautifulSoup(html,'lxml').find("div",{"class":"bg-white p15 center imgac clearfix"}).find("h1",{"class":"center"}).get_text()
    pattern = re.compile(".*\(")
    title = pattern.findall(title0)
    title = title[0]
    title = title[:-1]
    page = title0[-6:]
    pattern = re.compile("\/\d*")
    page = pattern.findall(page)[0]
    pattern = re.compile("\d*")
    page = pattern.findall(page)[1]
    try:
        os.makedirs(dir + title + '_' + page)
    except:
        return
    html = urllib.request.urlopen(url).read()
    picurl = BeautifulSoup(html,'lxml').find("div",{"class": "bg-white p15 center imgac clearfix"}).find("img")["src"]
    img = urllib.request.urlopen(picurl).read()
    f = open(dir + title + '_' + page + "\\" + "1.jpg", "wb")
    f.write(img)
    f.close()
    pages = int(page) + 1
    for i in range(2, pages):
        try:
            url0 = url[:-5]
            url1 = url0 + '_' + str(i) + '.html'
            html = urllib.request.urlopen(url1).read()
            picurl = BeautifulSoup(html,'lxml').find("div", {"class": "bg-white p15 center imgac clearfix"}).find("img")["src"]
            img = urllib.request.urlopen(picurl).read()
            f = open(dir + title + '_' + page + "\\" + str(i) + ".jpg", "wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.reason)
                sql(url)
                print('未下载网址已存入数据库')
            elif hasattr(e, "reason"):
                print(e.reason)
                sql(url)
                print('未下载网址已存入数据库')
        finally:
            pass

def xiazai_uumnt_sql(url):
    html = urllib.request.urlopen(url).read()
    title0 = BeautifulSoup(html,'lxml').find("div",{"class":"bg-white p15 center imgac clearfix"}).find("h1",{"class":"center"}).get_text()
    pattern = re.compile(".*\(")
    title = pattern.findall(title0)
    title = title[0]
    title = title[:-1]
    page = title0[-6:]
    pattern = re.compile("\/\d*")
    page = pattern.findall(page)[0]
    pattern = re.compile("\d*")
    page = pattern.findall(page)[1]
    try:
        os.makedirs(dir + title + '_' + page)
    except:
        shutil.rmtree(dir + title + '_' + page)
        os.makedirs(dir + title + '_' + page)
    html = urllib.request.urlopen(url).read()
    picurl = BeautifulSoup(html,'lxml').find("div",{"class": "bg-white p15 center imgac clearfix"}).find("img")["src"]
    img = urllib.request.urlopen(picurl).read()
    f = open(dir + title + '_' + page + "\\" + "1.jpg", "wb")
    f.write(img)
    f.close()
    pages = int(page) + 1
    for i in range(2, pages):
        try:
            url0 = url[:-5]
            url1 = url0 + '_' + str(i) + '.html'
            html = urllib.request.urlopen(url1).read()
            picurl = BeautifulSoup(html,'lxml').find("div", {"class": "bg-white p15 center imgac clearfix"}).find("img")["src"]
            img = urllib.request.urlopen(picurl).read()
            f = open(dir + title + '_' + page + "\\" + str(i) + ".jpg", "wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                sql(url)
                print('未下载网址已存入数据库')
            elif hasattr(e, "reason"):
                print(e.reason)
                sql(url)
                print('未下载网址已存入数据库')
        finally:
            pass