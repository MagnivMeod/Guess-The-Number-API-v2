from flask import Flask, jsonify, session, request
import random


app = Flask("Guess The Number API - v2")
app.secret_key = "12i3SDIIhKDOSKd08213asdqw2e12sadhUHD2108h#1hsa"

@app.route("/api/start_game", methods=["GET"])
def start_game():
    if not session.get("number"):
        session["number"] = random.randint(0, 100)
        session["tries"] = 0

    return jsonify({"success": True,})

@app.route("/api/guess_the_number", methods=["POST"])
def guess_the_number():
    guess = int(request.json["guess"])
    session["tries"] += 1

    if guess < session["number"]:
        status = "lower"
    elif guess > session["number"]:
        status = "higher"
    else:
        status = "you win"

    return jsonify({"status": status, "tries": session["tries"]})


debug = True
app.run(host="0.0.0.0", port=1337, debug=debug)