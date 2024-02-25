import requests

# the following api returns stock price for tsla (not adjusted though)
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=H3ZWA9P1D0MEY2FG'
r = requests.get(url)
data = r.json()

print(data)