#from chatbot import CB
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/chatbot")
def home():
    print("Chatbot route:")
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print("get route:", userText)
    return userText + " Received"
app.run(debug = True)