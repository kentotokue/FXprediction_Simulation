'''
Created on 2020/06/23

@author: kentoo
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sp = 1
day = []
owarine = []
data = []
data2 = []
ten = 0
tei = 0
result = []
jyoushoudo=[]
jyoushou=[]


file=pd.read_csv('D:\ducas/USDJPY_30 Mins_Ask_2015.10.05_2020.10.11.csv',delimiter=',')#デューカスでダウンロードしたファイルをここに入れる
for i in range(len(file)):
    day.append(file['Local_time'][i])
    owarine.append(file['Close'][i])
for i in range(len(day)):
    set1 = []
    set1.append(day[i])
    set1.append(owarine[i])
    jyoushoudo.append(day[i])
    data2.append(set1)
def bottom(x):
    y = ten*(200-sp)/(200+sp)
    if(owarine[x] < y):
        return 1
    return 0
def top(x):
    y = tei*(200+sp)/(200-sp)
    if(owarine[x] > y):
        return 1
    return 0
saidai = np.argmax(owarine)
result.append(data2[saidai])
a = saidai
ten = owarine[saidai]
mode = 0
for i in range(saidai,-1,-1):

    if mode == 0:
        if (bottom(i) == 1):
            tei = owarine[i]
            a = owarine.index(owarine[i])
            result.append([data2[i],0])
            mode = 1
        elif (owarine[i] >= ten):
            ten = owarine[i]
            a = owarine.index(owarine[i])
            result.pop()
            result.append([data2[i],1])
    if mode == 1:
        if (top(i) == 1):
            ten = owarine[i]
            a = owarine.index(owarine[i])
            result.append([data2[i],1])
            mode = 0
        elif (owarine[i] <= tei):
            tei = owarine[i]
            a = owarine.index(owarine[i])
            result.pop()
            result.append([data2[i],0])
result.pop()
result.reverse()
a = saidai
ten = owarine[saidai]
mode = 0
for i in range(saidai,len(owarine),1):

    if mode == 0:
        if (bottom(i) == 1):
            tei = owarine[i]
            a = owarine.index(owarine[i])
            result.append([data2[i],0])
            mode = 1
        elif (owarine[i] > ten):
            ten = owarine[i]
            a = owarine.index(owarine[i])
            result.pop()
            result.append([data2[i],1])
    if mode == 1:
        if (top(i) == 1):
            ten = owarine[i]
            a = owarine.index(owarine[i])
            result.append([data2[i],1])
            mode = 0
        elif (owarine[i] < tei):
            tei = owarine[i]
            a = owarine.index(owarine[i])
            result.pop()
            result.append([data2[i],0])

result.pop()

d = open("sp.txt","w",encoding="utf-8")
d.write("日付　天井と底"+"\n")
for i in range (0,len(result),1):
    d.write(str(result[i][0][0])+" "+str(result[i][1])+"\n")
d.close()




#上昇度を求める
if result[0][1]==0:
        for i in range(0,jyoushoudo.index(result[0][0][0]),1):
            jyoushou.append([jyoushoudo[i],0])
elif result[0][1]==1:
        for i in range(0,jyoushoudo.index(result[0][0][0]),1):
            jyoushou.append([jyoushoudo[i],1])

for i in range(len(result)-1):
    if result[i][1]<result[i+1][1]:
        before=result[i][0][0]
        after=result[i+1][0][0]
        afterindex=jyoushoudo.index(after)
        beforeindex=jyoushoudo.index(before)
        for i in range(beforeindex,afterindex,1):
            jyoushou.append([jyoushoudo[i],1])
    elif result[i][1]>result[i+1][1]:
        before=result[i][0][0]
        after=result[i+1][0][0]
        afterindex=jyoushoudo.index(after)
        beforeindex=jyoushoudo.index(before)
        for i in range(beforeindex,afterindex,1):
            jyoushou.append([jyoushoudo[i],0])



for i in range(len(jyoushou)):
    print(jyoushou[i])


s = open("jyoushou.txt","w",encoding="utf-8")
#s.write("日付　天井と底"+"\n")
for i in range (0,len(jyoushou),1):
    s.write(str(jyoushou[i][0])+","+str(jyoushou[i][1])+"\n")
s.close()







