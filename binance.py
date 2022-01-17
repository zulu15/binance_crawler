import requests
import json

URL = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "123",
    "content-type": "application/json",
    "Host": "p2p.binance.com",
    "Origin": "https://p2p.binance.com",
    "Pragma": "no-cache",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}
data = {
	"page":1,
	"rows":10,
	"payTypes":[],
	"asset":"USDT",
	"tradeType":"SELL",
	"fiat":"ARS",
	"publisherType":None
}

binance = requests.post(URL, json=data,headers = headers).json()
#print(len(binance["data"]))
sell_prices = ""
for data in binance["data"]:
  #print(data["adv"]["price"])
  sell_prices += data["adv"]["price"] + "\n"
  


WEB_HOOK_SLACK_URL = "https://hooks.slack.com/services/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"
payload = {
  "channel": "#testmy",
  "username": "webhookbot",
  "text": str(sell_prices)
}
post = requests.post(WEB_HOOK_SLACK_URL, json=payload)
if post.status_code != 200:
  WEB_HOOK_SLACK_URL = "https://hooks.slack.com/services/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"
  payload = {
    "channel": "#testmy",
    "username": "webhookbot",
    "text": "Error "+ post.text,
  }
  error = requests.post(WEB_HOOK_SLACK_URL, json=payload)


  
 