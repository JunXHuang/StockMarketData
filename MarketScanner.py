import requests,json,supportFunctions,plotly
plotly.tools.set_credentials_file(username='junxhuang', api_key='aGMie3Yu5C9pc4L0GevK')
ticker = 'aapl'

dataUrl = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?date.gte=20100101&date.lt=20170630&ticker='+ticker+'&api_key=41EKAEo-bjk6qXukkyeT'

reponseData = requests.get(dataUrl)

jsonData = json.loads(reponseData.text)
dailyStockData = jsonData['datatable']['data']

sum=0
# 0 ticker
# 1 date
# 2 open
# 3 high
# 4 low
# 5 close
maxHigh = 0
maxLow = 0
avgHigh = 0
avgLow = 0
HoDCounter = 0
LoDCounter = 0
skipFirst = True
for i in dailyStockData:
    if skipFirst:
        closePrice = i[5]
        skipFirst = False
        continue
    HoD = (i[3]-closePrice)/closePrice
    LoD = (closePrice-i[4])/closePrice
    if HoD > 0:
        avgHigh += HoD
        HoDCounter += 1
    if LoD > 0:
        avgLow += LoD
        LoDCounter += 1
    if HoD>maxHigh:
        maxHigh = HoD
    if LoD>maxLow:
        maxLow = LoD

    closePrice = i[5]
    if HoDCounter>0:
        avgHigh = avgHigh / HoDCounter
    if LoDCounter>0:
        avgLow = avgLow / LoDCounter
print ('ticker = '+ ticker)
#print ('maxHigh = %.2f' % round(maxHigh*100,2))
#print ('maxLow = %.2f' % round(maxLow*100,2))
#print ('avgHigh = %.2f' % round(avgHigh*100,2))
#print ('avgLow = %.2f' % round(avgLow*100,2))
supportFunctions.maxMovement(dailyStockData,ticker,5)

