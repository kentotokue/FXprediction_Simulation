'''
Created on 2020/07/20

@author: kentoo
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

day1=[]
day2=[]
yosoku=[]
owarine=[]

file=pd.read_csv('D:\ducas/USDJPY_30 Mins_Ask_2015.10.05_2020.10.11.csv',delimiter=',')#デューカスでダウンロードしたファイルをここに入れる
for i in range(len(file)):
    day1.append(str(file['Local_time'][i]))
    owarine.append(float(file['Close'][i]))

with open(r"C:\pleiades\workspace\deeplearning-keras\5/yosoku.txt","r",encoding="utf-8") as f: #乖離率のデータ
    next(f)
    for line in f:
        data2 = line.split(',')
        day2.append(str(data2[0]))
        yosoku.append(float(data2[1]))

firstday=day2[1]
lastday=day2[len(day2)-1]
firstday_index=day1.index(firstday)
lastday_index=day1.index(lastday)
#lastday_index=firstday_index+
print(firstday_index)
print(lastday_index)


fig=plt.figure()
num=0

#上昇度が１で赤０で青でプロット
for i in range(firstday_index,lastday_index,1):
    plt.plot(day1[i:i+2],owarine[i:i+2],color='red' if yosoku[num]==0 else 'blue')
    num=num+1

plt.xlabel('day')
plt.ylabel('value')
plt.xlim(0,17520)
plt.grid()
fig.savefig("yosoku.png")
plt.show()
