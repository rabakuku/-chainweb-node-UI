import os
import json
import html
from flask import Flask, render_template, abort, url_for, json, jsonify
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

app = Flask(__name__)

@app.route('/')

def kda_price():
    # Getting each line from get_block.txt and adding it to MyBlocks Lists
    with open('/root/flask_project/get_block.txt', 'r') as get_lines:
        MyBlocks = [line.strip() for line in get_lines]
    get_lines.close()    
    
    # Count the coins since day 1
    with open(r"/root/flask_project/get_block.txt", 'r') as get_coins:
        for count, line in enumerate(get_coins):
            pass
    count *= 1.0658245  # 1.0658245 coin per block
    
    #getting KADENA price and rank from Coinmarketcap	
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'slug': 'kadena',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '9b28e833-73e1-48dc-95bd-3adf6f7c732d',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        price_data = json.loads(response.text)['data']['5647']['quote']['USD']['price']
        #rounding the float to 2 decimals
        price_data_done = str(round(price_data, 2))

        rank_data = json.loads(response.text)['data']['5647']['cmc_rank']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("nothing")
    
    return render_template('index.html', title="RapaCrypto", kda_price=price_data_done, kda_rank=rank_data, total_coins=count, latest_1=MyBlocks[-1],
      latest_2=MyBlocks[-2], latest_3=MyBlocks[-3],  latest_4=MyBlocks[-4],   latest_5=MyBlocks[-5],   latest_6=MyBlocks[-6],  latest_7=MyBlocks[-7], 
      latest_8=MyBlocks[-8], latest_9=MyBlocks[-9],  latest_10=MyBlocks[-10], latest_11=MyBlocks[-11], latest_12=MyBlocks[-12])
    get_coins.close()

if __name__ == '__main__':
   app.run()
