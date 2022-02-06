from flask import Flask, request, render_template
import sqlite3 as sql

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def get_user():
    if request.method == "POST":
        user_details = dict()
        user_details['name'] = request.form.get("visitor_name")
        user_details['email'] = request.form.get("visitor_email")
        user_details['contact'] = request.form.get("visitor_phone")
        with sql.connect("identifier.sqlite") as con:
            cur = con.cursor()
            cur.execute(
                f"INSERT INTO user (name, email, contact) VALUES "
                f"({','.join(user_details.values())})")
            con.commit()
        return render_template("confirm.html")
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
