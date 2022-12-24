from binance import Client
import datetime
from matplotlib import pyplot as plt
import pandas as pd
import json

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

client = Client(config['binance_api']['api_key'], config['binance_api']['api_secret'])

def unix_to_datetime(unix_time):
    return datetime.datetime.fromtimestamp(unix_time/1000.0)

def date_to_unix(date):
    date = datetime.datetime.now()
    date = date.replace(hour=0, minute=0, second=0, microsecond=0)
    date = date - datetime.timedelta(days = config['days'])
    return int(date.timestamp()*1000)

results = []

klines = client.get_historical_klines(config['crypto'], Client.KLINE_INTERVAL_5MINUTE, date_to_unix(datetime.datetime.now()))
values = [[unix_to_datetime(el[0]), float(el[1])] for el in klines]

df = pd.DataFrame(values, columns=['ds', 'y'])
plt.plot(df['ds'], df['y'])
plt.xticks(rotation=45)
plt.show()