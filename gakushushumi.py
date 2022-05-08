'''
Created on 2020/07/07

@author: kentoo
'''
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

data = []
data1 = []
data2 = []
target = []
kairi = []
jyousyou = []
maxlen = 60
day1 = []
day2 = []
day3 = []
owarine = []
def normalization(a):
    b = []
    for i in a:
        b.append((i-min(a))/(max(a)-min(a)))
    return b
file=pd.read_csv('D:\ducas/EURUSD_30 Mins_Ask_2015.07.14_2020.07.20.csv',delimiter=',')#デューカスでダウンロードしたファイルをここに入れる
for i in range(len(file)):
    day1.append(str(file['Local_time'][i]))
    owarine.append(float(file['Close'][i]))
#for line in open (" .txt","r",encoding="utf-8"): #デューカスコピーでダウンロードしたデータ
#    data1 = line.split(',')
#    day1.append(str(data1[0]))
#    owarine.append (float(data1[4]))
with open(r"C:\pleiades\workspace\deeplearning-keras\5/kairiritsu.txt","r",encoding="utf-8") as f: #乖離率のデータ
    next(f)
    for line in f:
        data2 = line.split(',')
        day2.append(str(data2[0]))
        kairi.append(float(data2[1]))
with open(r"C:\pleiades\workspace\deeplearning-keras\5/jyoushou.txt","r",encoding="utf-8") as f: #上昇度のデータ
    next(f)
    for line in f:
        data3 = line.split(',')
        day3.append(str(data3[0]))
        jyousyou.append(str(data3[1]))
'''
日付合わせ
'''
for i in range(len(owarine)-1,0,-1):
    if(day1[i] == day3[-1]):
        del day1[i+1:len(day1)]
        del owarine[i+1:len(owarine)]
        break
for i in range(len(kairi)-1,0,-1):
    if(day2[i] == day3[-1]):
        del day2[i+1:len(day2)]
        del kairi[i+1:len(kairi)]
        break
if(len(day2) > len(day3)):
    for i in range(0,len(owarine)):
        if(day1[i] == day3[0]):
            del day1[0:i]
            del owarine[0:i]
            break
    for i in range(0,len(kairi)-1):
        if(day2[i] == day3[0]):
            del day2[0:i]
            del kairi[0:i]
            break
else:
    for i in range(0,len(owarine)):
        if(day1[i] == day2[0]):
            del day1[0:i]
            del owarine[0:i]
            break
    for i in range(0,len(jyousyou)):
        if(day3[i] == day2[0]):
            del day3[0:i]
            del jyousyou[0:i]
            break
for i in range(0, len(kairi)-maxlen):
    data.append(normalization(kairi[i: i + maxlen]))
    target.append(jyousyou[i + maxlen])
X = np.array(data).reshape(len(data), maxlen, 1)
Y = np.array(target).reshape(len(data), 1)
N_train = int(len(data) * 0.5)
N_validation = len(data) - N_train
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=N_validation,shuffle=False)
'''
モデル設定
'''
n_in = len(X[0][0])
n_hidden = 60
n_out = len(Y[0])
def weight_variable(shape, name=None):
    return np.random.normal(scale=.01, size=shape)
model = Sequential()
model.add(LSTM(n_hidden,
                    kernel_initializer="random_uniform",
                    input_shape=(maxlen, n_in)))
model.add(Dense(n_hidden, kernel_initializer="random_uniform"))
model.add(Activation('sigmoid'))
model.add(Dense(n_out, kernel_initializer="random_uniform"))
model.add(Activation('sigmoid'))
optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999)
model.compile(loss='mean_squared_error',
              optimizer=optimizer, metrics=['accuracy'])
'''
モデル学習
'''
epochs = 100
batch_size = 1000
model.fit(X_train, Y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_split = 0.25)

y_ = model.predict(X_validation)
yosoku = []
for i in range (0,len(y_)):
    if (y_[i]>=0.5):
        yosoku.append('1')
    else:
        yosoku.append('0')
#学習の予測データ表示
#c = open("predict.txt","w",encoding="utf-8")
#for y in range(len(y_)):
#    c.write(str(y_[y])+"/n")
#c.close()




b = open("yosoku.txt","w",encoding="utf-8")
b.write("日付 上昇度" + "\n")
print(len(yosoku))
for s in range(len(yosoku)):
    b.write(str(day3[(len(jyousyou))-(len(yosoku))+s])+","+str(yosoku[s])+"\n")
b.close()
