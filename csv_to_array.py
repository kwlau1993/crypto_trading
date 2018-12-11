#!/usr/bin/python
import csv
import numpy as np
import matplotlib.pyplot as plt

bitfinex = []
with open("XRP-USD_histominute_Bitfinex.csv") as file1:
    reader = csv.reader(file1, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        bitfinex.append(row)
file1.close()
np.array(bitfinex)
tmp = np.transpose(bitfinex)
ex1 = np.array([tmp[1],tmp[5]])

kraken = []
with open("XRP-USD_histominute_Bitstamp.csv") as file2:
    reader = csv.reader(file2, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        kraken.append(row)
file2.close()
np.array(kraken)
tmp = np.transpose(kraken)
ex2 = np.array([tmp[1],tmp[5]])
#units in %
delta = [100*(ex1[i] - ex2[i])/ex1[i] for i in range(0,len(ex1))]
avg = sum(delta[0])/len(delta[0])
high = max(delta[0])
c = len(delta[0])-1

print (avg,high)

plt.scatter(ex1[1],delta[0])
plt.hlines(avg,ex1[1][0],ex1[1][c])
plt.hlines(high,ex1[1][0],ex1[1][c])
plt.show()
