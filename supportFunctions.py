import plotly.plotly as py
import plotly.graph_objs as go

def maxMovement(data,ticker,days):
    if not data:
        return
    closePrice = data[0][5]
    list=[]
    occurances = {}
    for i in range(0,days):
        occurances[i]={}
    for marketData in data:
        priceChange = (marketData[5]-closePrice)/closePrice
        closePrice = marketData[5]
        if len(list)<days:
            list.insert(0,priceChange)
        else:
            list.pop()
            list.insert(0,priceChange)
            sum = 0
            for i in range(0,days):
                sum += list[i]
                h = round(sum*100)
                if h in occurances[i]:
                    occurances[i][h]=int(occurances[i].get(h))+1
                else:
                    occurances[i][h]=1
    xx=[]
    yy=[]
    for key in sorted(occurances[days-1]):
        xx.append(key)
        yy.append(occurances[days-1][key])
    chartData = [go.Bar(
        x=xx,
        y=yy)]
    py.iplot(chartData,filename=ticker+' '+str(days)+' days')