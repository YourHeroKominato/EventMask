# import main Flask class and request object
from flask import Flask, request, jsonify

import json
import finalNftGenerator

app = Flask(__name__)


@app.route("/", methods=["GET"])
def test_get():
    discord_account_name = request.args.get("discord_account_name")
    discord_event_name = request.args.get("discord_event_name")
    discord_account_address = request.args.get("discord_account_address")
    jsonData = jsonify(
        {
            "discord_account_name": discord_account_name,
            "discord_event_name": discord_event_name,
            "discord_account_address": discord_account_address,
        }
    )
    print(jsonData)
    return jsonData


if __name__ == "__main__":
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

# @app.route("/")
# def App():
#     response_hyon = "hyon"
#     return response_hyon


# @app.route("/safeMint", methods=["POST"])
# def proceed_mint():
# finalNftGenerator.nftImageGenerator(
#     discord_event_name,
#     discord_account_name,


#     safeMint()
