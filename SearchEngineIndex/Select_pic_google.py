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
        count = re.search('找到约(.+?)条结果', html, re.S)
        return count.group(1)
with open('countpic.txt','w') as f:
    with  open('kwd.txt', 'r') as f1:
        content = f1.readlines()
        for i in content:
            kwd = i.strip()
            url = 'https://www.google.com/search?q=' + kwd + ' 图片'
            res = res_count(url)
            f.write(res+'\n')
            print i + "的术语索引数为" + res
print ("完毕,结果保存在文件")
