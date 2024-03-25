from pycoingecko import CoinGeckoAPI
import pandas as pd

from fbprophet.plot import plot_plotly
import plotly.offline as py
import plotly.graph_objs as go

cg = CoinGeckoAPI()
bitcoin_price = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
#print(bitcoin_price)

data = pd.DataFrame(bitcoin_price, columns = ['TimeStamp', 'Price'])
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')

candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x=candlestick_data.index, 
                                 open=candlestick_data['Price']['first'], 
                                 high=candlestick_data['Price']['max'], 
                                 low=candlestick_data['Price']['min'],                      
                                 close=candlestick_data['Price']['last'],)
                                 ])
fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date', yaxis_title='Price(USD$)', title='Bitcoin Candlestick Chart Over 30 Days')



#print(data)
print(candlestick_data)


