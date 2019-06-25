# -*- coding: UTF-8 -*-
import requests
import re
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
def get_html(url, retry=3, timeout=10): # 获取serp源代码函数
    try:
       r = requests.get(url, headers=header, timeout=10)
    except requests.exceptions.RequestException:
       r = ''
       if retry > 0:
         get_html(url, retry-1)
    else:
        return r.text
def res_count(url):         #采集结果数函数
    html = get_html(url)
    if html:
        html = html.encode('utf-8')
        count = re.search('百度为您找到相关结果约(.+?)个',html,re.S)
     #   count1 = re.search('约有(.+?)张',html,re.S)
    #if count:
    return count.group(1)
    #return count1.group(1)
    #return 0
with open('countvid.txt','w') as f:
    with  open('kwd.txt', 'r') as f1:
        content = f1.readlines()
        for i in content:
            kwd = i.strip()
            url = 'https://www.baidu.com/s?wd=' + kwd + ' 视频'
            res = res_count(url)
            f.write(res+'\n')
            print i + "的术语视频碎片数为" + res
print ("完毕,结果保存在文件")
