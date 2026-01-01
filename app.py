from flask import Flask, request, jsonify, send_file
from chatbot import get_response
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
