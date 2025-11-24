#!/usr/bin/python3


from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1" : {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username is None or username not in users:
        return None

    stored_hash = users[username]["password"]

    if check_password_hash(stored_hash, password):
        return username
    return None

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 401

    username = data["username"]
    password = data["password"]

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    stored_hash = users[username]["password"]

    if not check_password_hash(stored_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})

    return jsonify({"access_token": access_token}), 200

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    user = get_jwt_identity()

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted", 200

@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
