"""
Flask app that serves the UI at '/' and exposes two APIs:
- POST /extract_memory
- POST /reply
"""

from flask import Flask, request, jsonify, render_template
from memory_extractor import extract_memories
from personality_engine import rewrite
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return send_file("test.html")



@app.route("/extract_memory", methods=["POST"])
def extract_memory_route():
    data = request.get_json() or {}
    msgs = data.get("messages", [])
    mems = extract_memories(msgs)
    return jsonify({"memories": mems})



@app.route("/reply", methods=["POST"])
def reply_route():
    data = request.get_json() or {}
    reply = data.get("reply", "")
    tone = data.get("tone", "mentor")
    
    out = rewrite(reply, tone)
    return jsonify({"rewritten": out})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
