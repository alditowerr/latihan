import requests, os
from flask import Flask, jsonify, request, json
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv() #ngebaca file yang .env yang dibuat port itu

app = Flask(__name__)
CORS(app) #allow access from anywhere origin (default)
v1_path = os.environ.get("V1_PATH")
port = os.environ.get("PORT")

# /v1/learn/hello
print(v1_path, port)

@app.route(f"{v1_path}/towergtg", methods=["GET"]) #/v1/learn/hello = result akhir
def towergtg():
    return "Tower Ganteng bgt"

@app.route(f"{v1_path}/towergtgdeh", methods=["POST"])
def towergtgdeh():
    
    #payload : last_name & first_name
    body = request.get_json()
    first_name = body.get("first_name")
    last_name = body.get("last_name")


    return f"they got a Daughter and her name is : {first_name} {last_name}"

app.run(host="0.0.0.0", port=port, debug=True)
