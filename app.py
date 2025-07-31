from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("accident_map.html")

@app.route("/incidents")
def incidents():
    if os.path.exists("harford_incidents.json"):
        with open("harford_incidents.json") as f:
            data = json.load(f)
        return jsonify(data)
    else:
        return jsonify([])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
