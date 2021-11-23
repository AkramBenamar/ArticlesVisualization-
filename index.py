#coding: utf-8

import json 
import re
from datetime import date
from datetime import datetime
import collections
from collections import Counter
from dateutil import parser



#lecture
with open ("journaux.json","r", encoding='utf-8') as read_file:
    data = json.load(read_file)
    data.sort(key=lambda x: x["published"])
    
#affichage
i=0
j=0
passage=""
semaine=0
frequencefile=""
for item in data:
    if i!=0:
         datepub=parser.parse(item["published"])
         if datepub.isocalendar().week==semaine:
             passage=passage+" "+item["title"]
             semaine=parser.parse(item["published"]).isocalendar().week

         else:
             j=j+1
             passage=re.sub(r'\b\w{1,4}\b', '', passage)
             words = re.findall(r'\w+', passage)
             cap_words = [word.upper() for word in words]
             word_counts = Counter(cap_words).most_common(10)
             
             #word_counts=dict([(l,k) for k,l in sorted([(j,i) for i,j in word_counts.items()], reverse=True)][:10])
             result=json.dumps(word_counts,ensure_ascii=False)
             
             if j==1:
                frequencefile=frequencefile+'[{"semaine":'+str(semaine)+',"freq":'+str(result)+'}'
             else:
                 frequencefile=frequencefile+',{"semaine":'+str(semaine)+',"freq":'+str(result)+'}'

             
             semaine=parser.parse(item["published"]).isocalendar().week
             passage=""
             passage=passage+" "+item["title"]

    else:
        
        semaine=parser.parse(item["published"]).isocalendar().week
        passage=passage+" "+item["title"]


    i=i+1
frequencefile=frequencefile+']'
file=open("frequence.json","w",encoding='utf-8')
file.write(str(frequencefile))
file.close 
     



















