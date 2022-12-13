import sqlite3

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__)


@app.before_first_request
def create_tables():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"""
    )

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    return render_template("index.html", data=data)


@app.route("/", methods=["POST"])
def submit():
    # Get data from form
    name = request.form["name"]
    email = request.form["email"]

    # Insert data into table
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?,?)", (name, email))
    conn.commit()
    conn.close()

    return redirect(url_for("success"))


@app.route("/success")
def success():
    return "Form data successfully submitted."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
