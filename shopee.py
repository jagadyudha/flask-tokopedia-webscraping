import urllib.parse
import requests
import json
import pandas as pd
import openpyxl

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79'}

def shopee(item_name):
    item_name_quote = urllib.parse.quote(item_name)
    url = ("https://shopee.co.id/api/v4/search/search_items?keyword={}&limit=5&with_search_cover=true").format(item_name_quote)
    data = requests.get(url, headers=headers).content.decode("utf-8")
    data = json.loads(data)['items']
    for obj in data:
        dict = (obj['item_basic'])
        df = pd.DataFrame(dict, columns = ['name','price'], index=[0-])
        print (df)
    #df = pd.DataFrame(dict, columns = ['name','price'])
    #df['price'] = df['price']/100000
    #print (df)
    #df.to_excel('asu.xlsx')

shopee("skincare emina")