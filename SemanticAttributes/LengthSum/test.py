# -*- coding: UTF-8 -*-
# aa = 'afebb'
# bb = '和'
# print len(aa)
# print len(bb)

value=u'脚本12'
length = len(value)
utf8_length = len(value.encode('utf-8'))
length = (utf8_length - length)/2 + length
print(length)