from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
 
bot = ChatBot("Flask ChatBot v3", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(bot)

trainer.train([
    "Hello",
    "Hi there!",
    "How are you doing",
    "I'm doing great, how about you",
    "That is good to hear",
    "Thank you",
    "You're welcome"
])

trainer.train([
    "Good bye!",
    "See you soon!",
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))