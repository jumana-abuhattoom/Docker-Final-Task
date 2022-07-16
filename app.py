from flask import Flask
import redis
import requests

app = Flask(__name__)
redis1 = redis.Redis(host="redis", port=6379)


@app.route('/')
def printPrice():
    
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url).json()
    price= str(response['bpi']['USD']['rate'])
    redis1.set("current_price", price)
    return "Current price is : " + price 

@app.route('/avg')
def printAvgPrice():
    url = 'https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10'
    response = requests.get(url).json()
    sum_price = 0
    for data in response['Data']['Data']:
        sum_price=+ data['close']
    avg_price = sum_price/ 10
    return "Average price is : " + str(avg_price)
    
