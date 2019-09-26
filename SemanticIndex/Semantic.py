# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

def showlength(value):
    length = (len(value))
    utf8_length = len(value.encode('gbk'))
    length = str((utf8_length - length)/2 + length)
    return length

with open('count.txt', 'w') as count:
    with open('kwd.txt','r') as kwd:
        content = kwd.readlines()
        for i in content:
            word = i.strip()
            length2word = showlength(word)
            count.write(length2word + '\n')
            print "词语" + i + "的长度为" + length2word


print ("计算结束")
