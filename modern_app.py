from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hola"

@app.route("/saludar/<nombre>")
def saludar(nombre):
    return jsonify({"message": "Hola " + nombre})

if __name__ == "__main__":
    app.run(debug=True)
