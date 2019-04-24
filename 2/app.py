from flask import Flask, render_template, request, redirect, url_for, jsonify
import simplejson
import warnings
import sys
import requests
import json
import flask
#from classes.dataAnalysis import AnalysisClass


## IGNOR DEPRICATED MESSAGE WHILE EXECUTING CODE.
warnings.filterwarnings("ignore")

app = Flask(__name__)




@app.route('/index', methods = ['POST', 'GET'])
def index():
   return render_template('index.html')

@app.route('/', methods = ['POST', 'GET'])
@app.route('/exchange',methods = ['POST', 'GET'])
def exchangePage():
    return render_template("exchange.html")

@app.route('/getTrade',methods = ['POST', 'GET'])
def tradePage():
    return render_template("trade.html")



##URL WHERE TESTING FORM CALL TO SUBMIT DATA AND GIVE RESULT THE CREDIT SCORE:
@app.route('/currencyConvertorRate', methods=['POST'])
def currencyConvertor1():
   try:
      fromVal=request.form["from"]
      toVal=request.form["to"]
      url = 'https://rest.coinapi.io/v1/exchangerate/'+fromVal+'/'+toVal+''
      headers = {'X-CoinAPI-Key' : '7870464E-34FD-4F89-9A8B-23D785B3C128'}
      response = requests.get(url, headers=headers)
      #x=str(b'{\r\n  "time": "2019-04-23T13:21:52.9510107Z",\r\n  "asset_id_base": "BTC",\r\n  "asset_id_quote": "USD",\r\n  "rate": 5581.3961590496495622713358747\r\n}')
      jsonData=json.loads(response.content)
      dict_data={}
      for key in jsonData:
         dict_data.update({key : jsonData[key]})
      return render_template("output.html", data=dict_data)
   except Exception as error:
      return render_template("error.html", error = str(error))
   except:
      return render_template("error.html", error = "UNKNOWN ERROR!!")

##URL WHERE TESTING FORM CALL TO SUBMIT DATA AND GIVE RESULT THE CREDIT SCORE:
@app.route('/currencyConvertorAmount', methods=['POST'])
def currencyConvertor2():
   try:
      fromVal=request.form["from"]
      toVal=request.form["to"]
      amountVal=float(request.form["amount"])
      url = 'https://rest.coinapi.io/v1/exchangerate/'+fromVal+'/'+toVal+''
      headers = {'X-CoinAPI-Key' : '7870464E-34FD-4F89-9A8B-23D785B3C128'}
      response = requests.get(url, headers=headers)
      #x=str(b'{\r\n  "time": "2019-04-23T13:21:52.9510107Z",\r\n  "asset_id_base": "BTC",\r\n  "asset_id_quote": "USD",\r\n  "rate": 5581.3961590496495622713358747\r\n}')
      jsonData=json.loads(response.content)

      #jsonData=json.loads(b'{\n  "time": "2019-04-23T13:21:52.9510107Z",\n "asset_id_base": "BTC",\n  "asset_id_quote": "USD",\n  "rate": 5581.3961590496495622713358747\n}')
      
      dict_data={}
      for key in jsonData:
         dict_data.update({key : jsonData[key]})
      result=amountVal*float(dict_data["rate"])
      return render_template("output.html", data=dict_data, result=str(amountVal)+" "+str(fromVal)+" is "+str(result)+" "+str(toVal))
   except Exception as error:
      return render_template("error.html", error = str(error))
   except:
      return render_template("error.html", error = "UNKNOWN ERROR!!")
@app.route('/filtersymbol', methods=['POST','GET'])
def filterSymobl():
   try:
      #amountVal=1000
      symbol_id=request.form["symbol_id"]
      
      url = 'https://rest.coinapi.io/v1/symbols'
      #url = 'https://rest.coinapi.io/v1/trades/latest'
      headers = {'X-CoinAPI-Key' : '7870464E-34FD-4F89-9A8B-23D785B3C128'}
      response = requests.get(url, headers=headers)
      jsonData=json.loads(response.content)
      #jsonData=json.loads(b'[\r\n {\r\n "symbol_id": "COINMEX_SPOT_WBBT_ETH",\r\n "exchange_id": "COINMEX"\r\n},\r\n {\r\n "symbol_id": "COINTIGER_SPOT_ELET_BTC",\r\n  "exchange_id": "COINTIGER"\r\n}\r\n]')
      #jsonData=json.loads(b'{\n  "time": "2019-04-23T13:21:52.9510107Z",\n "asset_id_base": "BTC",\n  "asset_id_quote": "USD",\n  "rate": 5581.3961590496495622713358747\n}')
      i=0
      listx=[]
      rowx=""
      for row in jsonData:
       rowx=rowx+"{ "
       y=0
       for key in row:
             
             rowx=rowx+"'"+str(key)+"':'"+str(jsonData[i][key])
             if y!=int(len(row))-1:
               rowx=rowx+"',"
             else:
               rowx=rowx+"'"
             y=y+1
       if i!=int(len(jsonData))-1:
             rowx=rowx+"}"
       else:
             rowx=rowx+"}"
       listx.append(rowx)
       i=i+1
       rowx=""
      #print(listx)
      #print("---")
      f=open("xxc.txt","w+")
      f2=open("xxc2.txt","w+")
      # f.write(str(jsonData))
      f.write(symbol_id)
      listjson=[]
      for x in listx:
         t=eval(str(x))

         if str(t['symbol_id']) != str(symbol_id):
            f.write(t['symbol_id']+" "+symbol_id+"\n")
         else:
            listjson.append(eval(str(x)))
            f2.write(t['symbol_id']+" "+symbol_id+"\n")
         t=None
      f.close()
      return render_template('symbol.html', data=listjson)
      #return render_template("output.html", data=dict_data)
   except Exception as error:
      return render_template("error.html", error = str(error))
   except:
      return render_template("error.html", error = "UNKNOWN ERROR!!")

@app.route('/viewsymbolpage', methods=['POST','GET'])
def symbolPage():
    return render_template("symbol.html")

@app.route('/tradeGetLetest', methods=['POST','GET'])
def tradeGet1():
   try:
      #amountVal=1000
      url = 'https://rest.coinapi.io/v1/trades/latest'
      headers = {'X-CoinAPI-Key' : '7870464E-34FD-4F89-9A8B-23D785B3C128'}
      response = requests.get(url, headers=headers)
      jsonData=json.loads(response.content)
      #jsonData=json.loads(b'[\r\n {\r\n "symbol_id": "COINMEX_SPOT_WBBT_ETH",\r\n "exchange_id": "COINMEX"\r\n},\r\n {\r\n "symbol_id": "COINTIGER_SPOT_ELET_BTC",\r\n  "exchange_id": "COINTIGER"\r\n}\r\n]')
      #jsonData=json.loads(b'{\n  "time": "2019-04-23T13:21:52.9510107Z",\n "asset_id_base": "BTC",\n  "asset_id_quote": "USD",\n  "rate": 5581.3961590496495622713358747\n}')
      i=0
      listx=[]
      rowx=""
      for row in jsonData:
       rowx=rowx+"{ "
       y=0
       for key in row:
             
             rowx=rowx+"'"+str(key)+"':'"+str(jsonData[i][key])
             if y!=int(len(row))-1:
               rowx=rowx+"',"
             else:
               rowx=rowx+"'"
             y=y+1
       if i!=int(len(jsonData))-1:
             rowx=rowx+"}"
       else:
             rowx=rowx+"}"
       listx.append(rowx)
       i=i+1
       rowx=""
      #print(listx)
      #print("---")

      listjson=[]
      for x in listx:
       listjson.append(eval(str(x)))
      return render_template('output2.html', data=listjson)

      #return render_template("output.html", data=dict_data)
   except Exception as error:
      return render_template("error.html", error = str(error))
   except:
      return render_template("error.html", error = "UNKNOWN ERROR!!")

##########################################################


## debug = True
## THIS IS TO START SERVICE ON SERVER WITH 'http://host:port/'
if __name__ == '__main__':
   app.run(host='localhost', port='5007', debug = True)
