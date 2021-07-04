from flask import Flask, render_template, request
import urllib.parse
import requests
import json
import pandas as pd
import openpyxl

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79'}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/getdata", methods = ['POST', 'GET'])
def getdata():
    if request.method == 'POST':
        form_data = request.form["name"]
        tokopedia(form_data)
        return render_template("getdata.html")

def tokopedia(item_name):
    item_name_quote = urllib.parse.quote(item_name)
    url = ("https://ace.tokopedia.com/search/product/v3?navsource=home&ob=3&st=product&q={}&rows=100&start=0&full_domain=www.tokopedia.com&scheme=https&device=desktop&source=shop_product").format(item_name_quote)
    data = requests.get(url, headers=headers).content.decode("utf-8")
    data = json.loads(data)
    dict = data['data']['products']
    df = pd.DataFrame(dict, columns = ['name', 'price'])
    df = df.sort_values(by=['price'])
    df.to_html('templates/getdata.html')

if __name__ == "__main__":
    app.run(debug=True)