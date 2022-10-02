#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
s="""hi69@qq.com, werksdf@163.com, sdf@sina.com
sfjsdf@139.com, soifsdfj@134.com
pwoeir23@126.com"""

def add(n):
    n=n.group("number")
    n=int(n)
    n+=212
    return str(n)
t=re.findall(r'(?P<number>\d+)',s)
print(t)
t=re.findall(r'\d+',s)
print(t)
