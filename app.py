from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('base.html')

@app.route("/predict", methods=["POST"])
def predict():
    user_message = request.get_json().get("message")
    response = requests.post("https://localhost:5005/webhooks/rest/webhook", json={"message":user_message})
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)