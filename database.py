from xml.dom import minidom
import re
file = open('tewiki-20190420-pages-articles-multistream.xml','r',encoding='utf-8')
mydoc=minidom.parse(file)
file.close()
title = mydoc.getElementsByTagName('title')
text = mydoc.getElementsByTagName('text')
regex = re.compile('[a-zA-Z<\/>]')
regex2=re.compile('[\:\/\?\"\*\\\\]')
directory="text_files"
path=0
l=len(title)
for i in range(l):
    # filename = " ".join(t.nodeValue for t in title[i].childNodes if t.nodeType == t.TEXT_NODE)
    path=path+1
    # print(path,type(path))
    paths= str(path)
    # print(paths,type(paths))
    path2 = directory+"/"+regex2.sub('',paths)+".txt"
    f= open(path2,"w+",encoding = 'utf-8')
    data = " ".join(t.nodeValue for t in text[i].childNodes if t.nodeType == t.TEXT_NODE)
    data2 = regex.sub('',data)
#     print(data2)
    print(path2)
    f.write(data2)
    f.close()