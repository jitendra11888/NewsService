from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

# --------------------------------------
# GET all users
# --------------------------------------
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

# --------------------------------------
# GET user by ID
# --------------------------------------
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(user)

# --------------------------------------
# CREATE new user
# --------------------------------------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data["name"]
    email = data["email"]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User created"})

# --------------------------------------
# UPDATE user
# --------------------------------------
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    name = data["name"]
    email = data["email"]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s",
                   (name, email, user_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User updated"})

# --------------------------------------
# DELETE user
# --------------------------------------
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User deleted"})

# --------------------------------------
# Run App
# --------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)
