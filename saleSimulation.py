
'''
Created on 2020/07/27

@author: kentoo
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#funds=100000

ask=[]
bid=[]
preask_high=[]
preask_close=[]
ask_high=[]
ask_close=[]
preask_low=[]
ask_low=[]
prebid_high=[]
prebid_close=[]
bid_high=[]
prebid_low=[]
bid_low=[]
bid_close=[]
data=[]
data2=[]
day=[]
day2=[]
day3=[]
day4=[]
yosoku=[]
jyoushou=[]

#予測データ読み込み
with open(r"C:\pleiades\workspace\deeplearning-keras\5/yosoku.txt","r",encoding="utf-8") as f: #乖離率のデータ
    next(f)
    for line in f:
        data = line.split(',')
        day.append(str(data[0]))
        yosoku.append(float(data[1]))

#csv読み込み
ask=pd.read_csv('D:\ducas/EURUSD_30 Mins_Ask_2015.07.14_2020.07.20.csv',delimiter=',')#デューカスでダウンロードしたファイルをここに入れる
#ask=pd.read_csv('D:\ducas/USDJPY_30 Mins_Ask_2015.10.05_2020.10.11.csv',delimiter=',')

for i in range(len(ask)):
    day2.append(str(ask['Local_time'][i]))
    preask_high.append(float(ask['High'][i]))
    preask_low.append(float(ask['Low'][i]))
    preask_close.append(float(ask['Close'][i]))

firstday=day[0]
lastday=day[len(day)-1]
firstday_index=day2.index(firstday)
lastday_index=day2.index(lastday)

#日付合わせ
for i in range(firstday_index,lastday_index,1):
    ask_high.append(preask_high[i])
    ask_low.append(preask_low[i])
    ask_close.append(preask_close[i])


#csv読み込み
bid=pd.read_csv('D:\ducas/EURUSD_30 Mins_Bid_2015.07.14_2020.07.20.csv',delimiter=',')#デューカスでダウンロードしたファイルをここに入れる
#bid=pd.read_csv('D:\ducas/USDJPY_30 Mins_Bid_2015.10.05_2020.10.11.csv',delimiter=',')
for i in range(len(bid)):
    day3.append(str(bid['Local_time'][i]))
    prebid_high.append(float(bid['High'][i]))
    prebid_low.append(float(bid['Low'][i]))
    prebid_close.append(float(bid['Close'][i]))



firstday_index2=day3.index(firstday)
lastday_index2=day3.index(lastday)

#日付合わせ
for i in range(firstday_index2,lastday_index2,1):
    bid_high.append(prebid_high[i])
    bid_low.append(prebid_low[i])
    bid_close.append(prebid_close[i])
    day4.append(str(day3[i]))

x1=[]
y=[]

funds=100000 #資金

fund=100000
flag=0

leverage=25 #レバレッジ

kabu=0 #持ち球

position=0

num=12 #予測の1を見る期間

salenum=0

#(len(yosoku)-1)
for i in range(0,48*547,num):


    x=0

    for l in range(i,i+num): #一定期間の予測の1の個数を保存

        if(yosoku[l]==1):
            x=x+1




    budget=funds*0.2
    movablemoney = budget*leverage
#先行売買
    if(kabu==0):
        if(x>=(num*0.5)):
            kabu=movablemoney*ask_close[i]


            position=movablemoney
            save_ask = ask_close[i]
            x1.append(str(day[i]))
            y.append(funds)
#反対売買
    elif(kabu != 0 and bid_close[i] <= save_ask*0.95):
        funds=funds+((position*bid_close[i])-kabu)
        kabu = 0
        print(day[i],'-----------------------losscut-----------------------------')


#利食い
    else:
        if( x<num*0.5):

            funds=funds+((position*bid_close[i])-kabu)

            kabu=0
            position=0
            salenum=salenum+1

            print(day[i]+": 利益 :"+str(funds-fund))
            x1.append(str(day[i]))
            y.append(funds)

#




fig=plt.figure()
print(funds)
print(salenum)

plt.xlabel('day')

plt.grid()
plt.plot(x1,y)
fig.savefig("sale.png")
plt.show()


