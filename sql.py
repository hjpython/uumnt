from factor import *
from config import kw

if __name__ == '__main__':
    urls = []
    conn = pymysql.connect(**kw)
    cur = conn.cursor()
    cur.execute("select url from uumnt")
    results = cur.fetchall()
    cur.execute("truncate uumnt")
    cur.close()
    conn.close()
    result = list(results)
    for r in result:
        urls.append("%s" % r)
    urls = list(set(urls))
    while urls:
        url = urls.pop()
        print("重新下载:%s" % url)
        xiazai_uumnt_sql(url)