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
    # Get port from environment variable, default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 to allow external access
    app.run(host="0.0.0.0", port=port)

