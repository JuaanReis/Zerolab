from flask import Blueprint, render_template, request, jsonify, abort
from database import get_connection, init_db

main = Blueprint('main', __name__)

init_db()

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/login")
def login():
    return render_template("login.html")

@main.route("/users", methods=["GET", "POST"])
def users():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        try:
            data = request.get_json()
            user = data.get("user")
            password = data.get("password")
            msg = data.get("msg")

            if not user or not password or not msg:
                return jsonify({"status": "error", "message": "Campos obrigatórios faltando"}), 400

            cursor.execute(
                "INSERT INTO users (username, password, message) VALUES (?, ?, ?)",
                (user, password, msg)
            )
            conn.commit()
            return jsonify({"status": "ok"})

        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

        finally:
            conn.close()

    elif request.method == "GET":
        cursor.execute("SELECT username, message FROM users ORDER BY id DESC")
        all_users = cursor.fetchall()
        conn.close()
        return render_template("users.html", users=all_users)

@main.route("/users/<username>", methods=["GET"])
def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, message FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        user_dict = {
            "id": user[0],
            "username": user[1],
            "message": user[2]
        }
        
        return render_template("userPage.html", user=user_dict)
    else:
        abort(404)

