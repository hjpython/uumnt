from factor import *
from multiprocessing import Pool

if __name__ == '__main__':
    p = Pool(50)
    #下载第1页的图片ctrl+/多行注释掉
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
        p.apply_async(xiazai_uumnt, args=(picurl,))

    #下载第2页到554页的图片
    for i in range(2,555):
        print("第" + str(i) + "页")
        url0 = 'https://www.uumnt.cc/meinv/list_'+str(i)+'.html'
        try:
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
            p.apply_async(xiazai_uumnt, args=(picurl,))
    p.close()
    p.join()
    print('恭喜您，已全部下载完毕')