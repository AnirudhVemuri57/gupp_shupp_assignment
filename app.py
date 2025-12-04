"""
app.py - minimal Flask API to demonstrate memory extraction and personality rewriting
Run: pip install flask && python app.py
Endpoints:
- POST /extract_memory  { "messages": [ ... ] }
- POST /reply           { "reply": "string", "tone": "mentor|witty|therapist" }
Returns JSON outputs.
"""
from flask import Flask, request, jsonify
from memory_extractor import extract_memories
from personality_engine import rewrite

app = Flask(__name__)
from flask_cors import CORS
CORS(app)

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
