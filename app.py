from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbmyhome



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_about')
def get_about():
    return render_template('index_about.html')

@app.route('/get_work')
def get_work():
    return render_template('index_work.html')






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
