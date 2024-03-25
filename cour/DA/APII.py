from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
bitcoin = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
#print(bitcoin)

data = pd.DataFrame(bitcoin, columns = ['TimeStamp', 'Price'])
print(data)


