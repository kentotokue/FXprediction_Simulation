'''
Created on 2020/06/28

@author: kentoo
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


day =[]
owarine =[]
data =[]
data2=[]
data3=[]

span=60 #移動平均の日数

#データの読み込み
file =pd.read_csv('D:\ducas/USDJPY_30 Mins_Ask_2015.10.05_2020.10.11.csv',delimiter=',')

for i in range(len(file)):
    day.append(file['Local_time'][i])
    owarine.append(file['Close'][i])

for i in range(len(day)):
    data.append(day[i])
    data.append(owarine[i])

#移動平均を求める
for i in range(len(day)-span+1):
    sum=0
    for y in range(span):

        sum=sum+owarine[i+y]
    ave=sum/span
    data2.append(ave)

#乖離率を求める
def kairi():
    for i in range(span-1,len(day)):
        kairiritu=0
        kairiritu=owarine[i]/data2[i-span-1]
        data3.append([day[i],kairiritu])

kairi()

for i in range(len(data3)):
    print(data3[i][1])
s = open("kairiritsu.txt","w",encoding="utf-8")

for i in range (0,len(data3),1):
    s.write(str(data3[i][0])+","+str(data3[i][1])+"\n")
s.close()



