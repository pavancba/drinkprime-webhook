from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    print("🔹 Incoming request:", req)

    intent = req['queryResult']['intent']['displayName']
    user_input = req['queryResult']['queryText']

    if intent == "confirm_slot_selection":
        response_text = (
            f"✅ Your technician visit has been scheduled for {user_input}. "
            "You'll get a confirmation SMS shortly. Thank you for using DrinkSeva! 💙"
        )
    else:
        response_text = "I'm not sure how to assist with that request right now."

    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run()