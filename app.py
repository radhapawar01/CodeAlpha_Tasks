from flask import Flask, request, jsonify, send_from_directory
from chatbot import get_response

app = Flask(__name__)

# Serve HTML and CSS directly from main folder
@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/style.css")
def style():
    return send_from_directory('.', 'style.css')

@app.route("/get_response", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
