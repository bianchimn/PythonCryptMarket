import urllib
import urllib2
import json
import time
import hmac,hashlib
import datetime
import time

polURL = 'https://poloniex.com/'
st = datetime.datetime(2016, 1, 1, 0, 0, 0)
en = datetime.datetime.now()
stDt = time.mktime(st.timetuple())
enDt = time.mktime(en.timetuple())

print stDt
print enDt
def returnTicker(pair):
    ret = urllib2.urlopen(urllib2.Request(polURL + 'public?command=returnTicker'))
    pars = json.loads(ret.read())
    return pars[pair]

def returnOrderBook(Pair):
    ret = urllib2.urlopen(urllib2.Request(polURL + 'public?command=returnOrderBook&currencyPair=' + Pair + '&depth=10'))
    return json.loads(ret.read())

def returnChartData(pair,period,start,end):
    ret = urllib2.urlopen(urllib2.Request(polURL + 'public?command=returnChartData&currencyPair=' + pair + '&period=' + period + '&start=' + stDt + '&end=' + enDt))
    return json.loads(ret.read())

def returnCurrencies(currency):
    ret = urllib2.urlopen(urllib2.Request(polURL + 'public?command=returnCurrencies'))
    pars = json.loads(ret.read())
    print pars[currency]



                           
