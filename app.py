# -*- coding: utf-8 -*-
import pickle
from flask import Flask,jsonify,request
from flask_cors import CORS
app = Flask(__name__)


clf= pickle.load(open('clf.pkl','rb'))


@app.route("/api",methods=['POST'])
cors = CORS(app)

def index():
    data = request.get_json(force=True)
    ip = data['ip']
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
