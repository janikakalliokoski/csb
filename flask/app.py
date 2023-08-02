from flask import Flask
from flask import render_template, request, redirect, session, abort
import sqlite3

import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.environ.get("SECRET_KEY")

app = Flask(__name__)

app.secret_key = secret_key

# app.config['PERMANENT_SESSION_LIFETIME'] = 120

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def is_admin(admin):
    if admin != True:
        abort(403)

@app.route("/")
def index():
    conn = get_db_connection()
    users = conn.execute('select * from users').fetchall()
    conn.close()
    return render_template("index.html", users=users)

@app.route("/create", methods=["GET", "POST"])
def create():
    conn = get_db_connection()
    if request.method == "GET":
        return render_template("create.html")

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # if len(username) < 3 or len(username) > 20:
        #     return render_template("create.html", message="Username should be between 3 and 20 letters")
        # if len(email) < 3 or len(username) > 50:
        #     return render_template("create.html", message="e-mail address should be between 3 and 50 letters")
        # if len(username) < 3 or len(username) > 20:
        #     return render_template("create.html", message="Password should be between 3 and 20 letters")

        sql = "insert into users (email, username, password, admin) values (?, ?, ?, ?)"
        conn.execute(sql, (email, username, password, False))
        conn.commit()
        conn.close()
        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    conn = get_db_connection()
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = "select id, email, username, password, admin from users where username=? and password=?"
        user = conn.execute(sql, (username, password)).fetchone()

        if not user:
            return render_template("login.html", message="wrong username or password")
        session["user_id"] = user[0]
        session["user_email"] = user[1]
        session["username"] = user[2]
        if user[4] == 1:
            session["user_admin"] = True
        elif user[4] == 0:
            session["user_admin"] = False
        return redirect("/")


@app.route("/logout")
def logout():
    try:
        session.pop("user_id", None)
        session.pop("user_email")
        session.pop("user_username", None)
        session.pop("user_admin", None)
    except:
        return False
    return redirect("/")

@app.route("/view")
def view():
    # admin = session.get("user_admin", 0)
    # is_admin(admin)

    conn = get_db_connection()
    users = conn.execute('select * from users').fetchall()
    conn.close()
    return render_template("view.html", users=users)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    # admin = session.get("user_admin", 0)
    # is_admin(admin)

    conn = get_db_connection()
    sql = "select id, email, username, admin from users where id=?"
    user = conn.execute(sql, (user_id,)).fetchone()
    conn.close()
    if user[3] == 1:
        admin = True
    else:
        admin = False
    return render_template("user.html", user=user, admin=admin)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    # admin = session.get("user_admin", 0)
    # is_admin(admin)

    conn = get_db_connection()
    if request.method == "GET":
        users = conn.execute('select * from users').fetchall()
        conn.close()
        return render_template("delete.html", users=users)
    if request.method == "POST":
        if "user" in request.form:
            user = request.form['user']
            sql = "delete from users where id=?"
            conn.execute(sql, (user),)
            conn.commit()
            conn.close()
        return redirect("/")

#@app.route("/update/<user_id>", methods=["GET", "POST"])
@app.route("/update/<int:user_id>", methods=["GET", "POST"])
def update(user_id: int):
    # uid = session.get("user_id", 0)
    # if uid != user_id:
    #     abort(403)
    conn = get_db_connection()

    # sql = f"select * from users where id='{user_id}'"
    # user = conn.execute(sql).fetchone()

    correct_sql = "select * from users where id=?"
    correct_user = conn.execute(correct_sql, (user_id,)).fetchone()
    conn.close()

    if request.method == "GET":
        return render_template("update.html", user=correct_user)

    if request.method == "POST":
        new_email = request.form["new_email"]
        conn = get_db_connection()

        # sql = f"update users set email='{new_email}' where id='{user_id}'"
        # conn.execute(sql)

        correct_sql = "update users set email=? where id=?"
        conn.execute(correct_sql, (new_email, user_id))

        conn.commit()
        conn.close()

        return redirect("/")

@app.route("/account/<int:user_id>", methods=["GET"])
def account(user_id):
    # uid = session.get("user_id", 0)
    # if uid != user_id:
    #     abort(403)
    conn = get_db_connection()

    sql = "select email, username, admin from users where id=?"
    user = conn.execute(sql, (user_id,)).fetchone()
    print(user[0], user[1], user[2])
    if user[2] == 1:
        admin = True
    else:
        admin = False
    conn.close()

    html = f"<head><title>Cyber Security Project</title></head>\
            <body><h2>Your User Info:</h2>\
            <p><strong>username: </strong><span>{user[1]}</span></p>\
            <p><strong>e-mail: </strong><span>{user[0]}</span></p>\
            <p><strong>admin: </strong><span>{ admin }</span></p>\
            <a href=\"/update/{user_id}\">Update Your E-mail address</a>\
            <br><a href=\"/\">Go Back</a></body>"

    return html


    # return render_template("account_info.html", user=user)
