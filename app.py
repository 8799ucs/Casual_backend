from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow requests from React

@app.route("/hello", methods=["POST"])
def hello():
    data = request.get_json()
    username = data.get("username", "Guest")
    return jsonify({"message": f"Hello {username}"})

if __name__ == "__main__":
    app.run(debug=True)
