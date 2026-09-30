from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {"id": 1, "name": "Laptop", "price": 75000},
    {"id": 2, "name": "Smartphone", "price": 35000},
    {"id": 3, "name": "Headphones", "price": 5000}
]

@app.route("/")
def home():
    return jsonify({
        "message": "E-Commerce Analytics Backend",
        "status": "running"
    })

@app.route("/api/products")
def get_products():
    return jsonify(products)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
