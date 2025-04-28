from flask import Flask, request, jsonify

app = Flask(__name__)

# Variable to store latest alert
latest_alert = {}

@app.route('/webhook', methods=['POST'])
def webhook():
    global latest_alert
    data = request.json
    latest_alert = {
        "ticker": data.get("ticker"),
        "price": data.get("price"),
        "time": data.get("time")
    }
    print(f"Received Alert: {latest_alert}")
    return jsonify({"status": "success", "received": latest_alert}), 200

@app.route('/latest', methods=['GET'])
def latest():
    return jsonify(latest_alert), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
