import urllib.request
from bs4 import BeautifulSoup
import os,re,time
import urllib.error
from config import dir
from multiprocessing import Pool

def rename(url):
    html = urllib.request.urlopen(url).read()
    title0 = BeautifulSoup(html, 'lxml').find("div", {"class": "bg-white p15 center imgac clearfix"}).find("h1", {
        "class": "center"}).get_text()
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
        os.rename(dir + title + page, dir + title + '_' + page)
    except:
        return

if __name__ == '__main__':
    p = Pool(50)
    # 更改第1页的名字
    print('第1页')
    url0 = 'https://www.uumnt.cc/meinv/'
    html = urllib.request.urlopen(url0).read().decode('utf-8')
    urls = BeautifulSoup(html,'lxml').find('div',{'id':'mainbodypul'}).findAll('a')
    bag = []
    for url in urls:
        bag.append(url['href'])
    urls = bag[::3]
    for url in urls:
        picurl = 'https://www.uumnt.cc'+url
        print(picurl)
        p.apply_async(rename, args=(picurl,))

    #更改第2页到554页的名字
    for i in range(2,555):
        print("第" + str(i) + "页")
        url0 = 'https://www.uumnt.cc/meinv/list_'+str(i)+'.html'
        try:
            html = urllib.request.urlopen(url0).read().decode('utf-8')
            if not html:
                time.sleep(2)
                html = urllib.request.urlopen(url0).read().decode('utf-8')
            urls = BeautifulSoup(html, 'lxml').find('div', {'id': 'mainbodypul'}).findAll('a')
        except:
            continue
        bag = []
        for url in urls:
            bag.append(url['href'])
        urls = bag[::3]
        for url in urls:
            picurl = 'https://www.uumnt.cc' + url
            print(picurl)
            p.apply_async(rename, args=(picurl,))
    p.close()
    p.join()
    print('恭喜您，已全部更改完毕')