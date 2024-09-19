import time

import yfinance as yf


def snapshot():
    with open('nifty500.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[1]
            name = line.split(",")[0]
            # data = yf.download(symbol, start="2021-10-01", end="2021-11-23")
            data = yf.download(symbol, period="6mo", threads=True)
            data.to_csv('data/{}.csv'.format(name))
    return {
        "code": "success"
    }


i = 1
while True:
    snapshot()
    time.sleep(750)
    print(f'Ran {i} time')
    i = i + 1
