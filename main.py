import pandas as pan
import numpy as np

data=pan.read_csv("input.csv")

#print(data.head())

myDict=dict()

for x in range(len(data)):
    #row = list(data.iloc[x])
    row=list()
    for i in range(4):
        if data.iloc[x][i]=="0":
            break

        if data.iloc[x][i] in myDict:
            myDict[data.iloc[x][i]]+=1
        else:
            myDict[data.iloc[x][i]]=1

        row.append(data.iloc[x][i])
    sorted(row)
    key=""
    for i in range(len(row)):
        key+=row[i]
    #print(key)

    if key in myDict:
        myDict[key]+=1
    else:
        myDict[key]=1



#print(myDict)


for x in myDict:

    #print(st)
     i=len(x)
     if i>2:
         st1=x[0:2]
         st2=x[2:i]
         print(st1+"-->"+st2)
         print(myDict[x]/myDict[st1])

