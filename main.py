from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
API_KEY = "d159c3c992dcfc3e31d5bee931ea0202"

@app.route("/events")
def events():
    fixture = request.args.get("fixture", "215662")
    resp = requests.get(
        "https://v3.football.api-sports.io/fixtures/events",
        headers={"x-apisports-key": API_KEY},
        params={"fixture": fixture}
    )
    return jsonify(resp.json())

@app.route("/live")
def live():
    resp = requests.get(
        "https://v3.football.api-sports.io/fixtures",
        headers={"x-apisports-key": API_KEY},
        params={"live": "all"}
    )
    return jsonify(resp.json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)