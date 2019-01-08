# -*- coding: utf-8 -*-
import pickle
from flask import Flask,jsonify,request
from flask_cors import CORS
import re
app = Flask(__name__)
CORS(app)

clf= pickle.load(open('clf.pkl','rb'))


import re

def makeip(ip):
    ip = re.sub('[^0-9.]', '', ip)
    #print(ip)
    data = str(ip.strip()).split('.')
    #print(data)
    data = list(filter(None, data))
    #print(data)
    cl=len(data)
    tl=4-(cl)
    #data.append('.0'*tl)
    #ip=''.join(data)
    
    ip = ip+'.0'*tl
    print(ip)
    ip = ip.replace('..','.')
    ip = ip.lstrip(".")
    ip =".".join(ip.split(".")[:4])
    
    return ip

@app.route("/api",methods=['POST'])


def index():
    data = request.get_json(force=True)
    ip = data['ip']
    ip=makeip(ip)
    ip1= [ip.split('.')]
    y_pred1 = clf.predict(ip1)
    y_pred = clf.predict_proba(ip1)
    prediction={'Predresult':y_pred1[0]}
    dictionary = dict(zip(clf.classes_, y_pred[0]))
    probability={'probability':dictionary}
    print('Zone for ip {} is {}'.format(y_pred1[0],ip))
    print(dictionary)
    final = prediction.copy()
    final.update(probability)
    
    return jsonify(final)

@app.route("/")


def test():
    
    return 'Deployment_Successful!!!'

if __name__ == '__main__':
   app.run(port=7987)
   
   
'''   
import requests, json
url = 'http://127.0.0.1:7987/api'
data = json.dumps({'ip':'10.23.65.25'})
r = requests.post(url, data)
print(r.text)
'''
