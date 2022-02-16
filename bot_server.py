from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
  return '<head><style>html{background-color:#000</style></head><h1 style="color: #fff;">Warden Bot here!</h1><br><img src="https://live.staticflickr.com/65535/51883316807_f028bc73f7_o.jpg" alt="lost ark image">'

def run():
  app.run(host='0.0.0.0', port=8080)

def bot_server():
  t = Thread(target=run)
  t.start()