from flask import Flask, json, request
from id_generator import create_id
import storage

app = Flask(__name__)

@app.route("/instruments")
def get_instruments():
    response = app.response_class(response=json.dumps(storage.instruments), status=200, mimetype="application/json")
    return response

@app.route("/instruments/<instrument_id>")
def get_instrument_by_id(instrument_id):
    response = app.response_class(response=json.dumps(storage.instruments[instrument_id]), status=200, mimetype="application/json")
    return response

@app.route("/instruments/user/<user_name>")
def get_instrument_by_user(user_name):
    users = {}
    for instrument in storage.instruments:
        if user_name.lower() == storage.instruments.get(instrument).get('user').lower():
            users[instrument] = storage.instruments.get(instrument)
    response = app.response_class(response=json.dumps(users), status=200, mimetype="application/json")
    return response

@app.route("/instruments", methods=["POST"])
def add_instrument():
    content = request.form
    content = content.to_dict()
    instrument_id = create_id()
    storage.instruments[instrument_id] = content
    response = {"instrumentId": instrument_id}
    return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')

@app.route("/instruments/reassign", methods=['POST'])
def reassign_instrument():
    content = request.form
    content = content.to_dict()
    response_body = {}
    for instrument in storage.instruments:
        if content["instrumentId"] == instrument:
            storage.instruments[instrument]["user"] = content["user"]
            response_body[instrument] = storage.instruments[instrument]
    response = app.response_class(response=json.dumps(response_body), status=200, mimetype="application/json")
    return response

@app.route("/instruments/add_video/<instrument_id>", methods=['POST'])
def add_video_to_instrument(instrument_id):
    content = request.form
    content = content.to_dict()
    storage.instruments[instrument_id]["video"] = content["video"]
    storage.instruments["izbKuDgm"]
    response_body = {instrument_id: storage.instruments[instrument_id]}
    response = app.response_class(response=json.dumps(response_body), status=200, mimetype="application/json")
    return response


if __name__ == '__main__':
    app.run(debug=True)
