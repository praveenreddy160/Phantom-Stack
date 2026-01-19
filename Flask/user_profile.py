from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# This is an API Endpoint.
# The Frontend calls this URL to get data.
@app.route("/api/profile")
def get_profile():
    # We return JSON (data), not HTML (visuals)
    return jsonify(
        username="Praveen",
        role="Software Developer",
        company="Fannie Mae"
    )

if __name__ == "__main__":
    app.run(debug=True)