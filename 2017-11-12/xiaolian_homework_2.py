# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:26:49 2017

@author: Lian Xiao
"""

'xiaolian_homework_2.py -- do my homework'

#Q1
y=x=[]
x+=[5]
'得到x=y=[5]'
x=x+[5]
'得到x=[5,5],y=[5]'

#Q2
a=1
b=0.5+0.5
a==b
'返回true'
a is b
'返回false'
id(a)
id(b)
isinstance(a,int) 
'返回true'
isinstance(b,int) 
'返回false'

#Q3
print [[1,0],[2.3]]