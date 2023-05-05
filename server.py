from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import io,jsonify,json
import queryEngine as QE
from flask_cors import CORS, cross_origin


app = Flask(__name__)


# Define a route to handle image uploads
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    print("Inside chat path....")
    if request.method == 'POST':       
         data = (request.get_json())
         print('passed data - ' , data['prompt'])
         return QE.runQuery(data['prompt'])


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response

if __name__ == '__main__':
    app.run(debug=True)
    CORS(app,support_credentials=True)