#!/usr/bin/env python
# coding: utf-8

import re
import os
head=open('title.txt','w')
document=open('document.txt','w')
summ1=open('summary1.txt','w')
summ2=open('summary2.txt','w')
summ3=open('summary3.txt','w')
fold=os.listdir()
fold1=[i for i in fold if 'article' in i]
for main in fold1:
    art1=os.listdir(main)
    for file in art1:
        with open(main+'/'+file,'r') as article:
            art=article.read()
            x=re.sub(r'\s',' ',art)
            x=re.sub('\@body','\n@body',x)
            x=re.sub('\@summary','\n@summary',x)
            with open("data.txt",'w') as f:
                f.write(x)
            with open("data.txt",'r') as f:
                doc=f.readlines()
            summary=[]
            for i in doc:
                i=re.sub(r'\s',' ',i)
                if '@title' in i:
                    title=i
                if '@summary' in i:
                    summary.append(i)
                if '@body' in i:
                    body=i
            if len(summary) >=3 and len(body.split())> 70 and len(title.split())> 7 and len(summary[0].split())> 7 and len(summary[1].split())> 7 and len(summary[2].split())> 7:
                head.write(re.sub('\@title','',title)+"\n")
                document.write(re.sub('\@body','',body)+"\n")
                summ1.write(re.sub('\@summary','',summary[0])+"\n")
                summ2.write(re.sub('\@summary','',summary[1])+"\n")
                summ3.write(re.sub('\@summary','',summary[2])+"\n")

head.close()
document.close()
summ1.close()
summ2.close()
summ3.close()

