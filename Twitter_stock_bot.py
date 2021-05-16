import yfinance as yf
import pprint

MSFT = yf.Ticker("MSFT")

pprint.pprint(MSFT.dividends)

GE = yf.Ticker("GE")

pprint.pprint(GE.dividends)

NEE = yf.Ticker("NEE")

pprint.pprint(NEE.dividends)

# pprint.pprint(MSFT.quarterly_earnings)

# pprint.pprint(GE.quarterly_earnings)

# pprint.pprint(NEE.quarterly_earnings)

# pprint.pprint(MSFT.history("6mo"))
# pprint.pprint(MSFT.info["dayHigh"] - MSFT.info["dayLow"])

# pprint.pprint(GE.info["marketCap"])

# pprint.pprint(NEE.info["marketCap"])

import csv
import itertools
data=MSFT.history("1mo")
MSFT.history('10y')
divData=MSFT.dividends
quarData=MSFT.quarterly_earnings
diffData=data["High"]-data["Low"]


with open('MSFTstockData.csv', mode='w') as MSFT_file:
    MSFT_writer = csv.writer(MSFT_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for count,(i,j) in enumerate(zip(diffData.keys(), divData.keys())):
        MSFT_writer.writerow([i,diffData[i]])

data=GE.history("1mo")
GE.history('10y')
divData=GE.dividends
quarData=GE.quarterly_earnings
diffData=data["High"]-data["Low"]


with open('GEstockData.csv', mode='w') as MSFT_file:
    MSFT_writer = csv.writer(MSFT_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for count,(i,j) in enumerate(zip(diffData.keys(), divData.keys())):
        MSFT_writer.writerow([i,diffData[i]])

data=NEE.history("1mo")
NEE.history('10y')
divData=NEE.dividends
quarData=NEE.quarterly_earnings
diffData=data["High"]-data["Low"]


with open('NEEstockData.csv', mode='w') as MSFT_file:
    MSFT_writer = csv.writer(MSFT_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for count,(i,j) in enumerate(zip(diffData.keys(), divData.keys())):
        MSFT_writer.writerow([i,diffData[i]])

import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

days = []
pricesM = []
pricesN = []
pricesG = []

with open('MSFTstockData.csv', 'r') as file:
    line = file.readline()
    while(line):
        line = line.rstrip('\n')
        stockData = line.split(',')
        print(stockData)
        days.append(stockData[0])
        pricesM.append(float(stockData[1]))
        line = file.readline()

with open('GEstockData.csv', 'r') as file:
    line = file.readline()
    while(line):
        line = line.rstrip('\n')
        stockData = line.split(',')
        pricesG.append(float(stockData[1]))
        line = file.readline()

with open('NEEstockData.csv', 'r') as file:
    line = file.readline()
    while(line):
        line = line.rstrip('\n')
        stockData = line.split(',')
        pricesN.append(float(stockData[1]))
        line = file.readline()

frame1 = plt.gca()
print(type(frame1.axes.get_xaxis()))

plt.plot(days, pricesM, label= "MSFT")
plt.plot(days, pricesN, label="NEE")
plt.plot(days, pricesG, label="GE")

plt.ylabel("Stock Price")
plt.xticks([])
plt.xlabel("Date")
plt.legend()

plt.savefig('graphs.png')
plt.show()

import tweepy

consumer_key = "Xxk2rDFdDwnhjHPWVhrHwAhyu"  # tokens have been reset
consumer_secret = "IMwv3Zvysj1kzOJNPbhqxjTY5GUBDWvXPzlCoHXViNXcGhsuF0"

access_token = "1380644457188622339-Xa4QAoaTdF8yULipTvyw4CAKG44q3V"
access_token_secret = "TqKhB4FvdT85flWU2otVw0eQtcWOLxoLHfHhlxyKhRkZQ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_with_media("/content/graphs.png", "This is a graph of the volitility of the MSFT, NEE, and GE stocks over a month long period")