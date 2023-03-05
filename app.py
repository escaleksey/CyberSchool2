import json
from urllib.parse import unquote

from cs50 import SQL
from flask import Flask, jsonify, make_response, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from utils.helpers import apology, login_required
from utils.filling_table.filling_table import FillTable
from utils.db_functions.db_functions import DataBase

# Configure application
app = Flask(__name__)
port = 5100

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///static/db/database.db")
db2 = DataBase("static/db/database.db")
# Create FillTable to filling tables
fill = FillTable(db2)


def json_decoder(js):
    return {
        a: b for a, b in filter(lambda x: x[1], js.items())
    }


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@app.route("/index")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks, cash, summa = [{"symbol": '2', "name": '123', "count": '1', "price": '23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price": '23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price": '23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price": '23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price": '23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price": '23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price": '23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price": '23', "total": '23'}], 0, 0

    return render_template(f"index.html", stocks=stocks, cash=cash, summa=summa)


@app.route("/title", methods=["GET", "POST"])
@login_required
def title():
    """Show portfolio of stocks"""
    values = (fill.fill_title_table())
    count_office_equipment = len(values["office_equipment"])
    if request.method == "POST":
        print(request.form)
        send_to_add_card = {}
        models = ''
        for e, v in request.form.items():
            if '_model' in e:
                models += v + ', '
            else:
                send_to_add_card[e] = v

            send_to_add_card['id_org_tech'] = models
        try:
            if not db2.check_exist('pk', int(request.form.get('id_pc'))):
                return apology("Неверный id ПК", 403)
            if not db2.check_exist('employee', int(request.form.get('employee'))):
                return apology("Неверный id Сотрудника", 403)
            for i in range(1, count_office_equipment + 1):
                model = f'{i}_model'
                if request.form.get(model):
                    if not db2.check_exist('org_tech', int(request.form.get(model))):
                        return apology("Неверный id орг оборудования", 403)
            db2.add_card(send_to_add_card)
            return redirect('/index')
        except Exception:
            return apology("Проверьте данные id ПК", 403)

    return render_template("title_form.html", values=values)


@app.route("/pc", methods=["GET", "POST"])
@login_required
def pc():
    """Show portfolio of stocks"""
    if request.method == 'POST':
        json_data = json_decoder(request.get_json())

        if not json_data:
            data = (fill.fill_pc_table())['values']
        else:
            data = fill.db.get_values_with_filter("pk", **json_data)

        return make_response(jsonify(data), 200)

    values = (fill.fill_pc_table())
    return render_template("tables.html", values=values)


@app.route("/equipment_received")
@login_required
def equipment_received():
    """Show portfolio of stocks"""
    if request.method == 'POST':
        json_data = json_decoder(request.get_json())

        if not json_data:
            data = (fill.fill_pc_table())['values']
        else:
            data = fill.db.get_values_with_filter("equipment_received", **json_data)

        return make_response(jsonify(data), 200)

    values = (fill.fill_equipment_received_table())
    return render_template("tables.html", values=values)


@app.route("/office_equipment")
@login_required
def office_equipment():
    """Show portfolio of stocks"""

    if request.method == 'POST':
        json_data = json_decoder(request.get_json())

        if not json_data:
            data = (fill.fill_pc_table())['values']
        else:
            data = fill.db.get_values_with_filter("org_tech", **json_data)

        return make_response(jsonify(data), 200)

    values = (fill.fill_office_equipment_table())
    return render_template("tables.html", values=values)


@app.route("/employees")
@login_required
def employees():
    """Show portfolio of stocks"""
    if request.method == 'POST':
        json_data = json_decoder(request.get_json())

        if not json_data:
            data = (fill.fill_pc_table())['values']
        else:
            data = fill.db.get_values_with_filter("pk", **json_data)

        return make_response(jsonify(data), 200)

    values = (fill.fill_employees_table())
    return render_template("tables.html", values=values)


@app.route("/cards")
@login_required
def cards():
    """Show portfolio of stocks"""
    values = (fill.fill_cards_table())
    return render_template("tables.html", values=values)


@app.route("/history")
@login_required
def history():
    """Show portfolio of stocks"""
    values = (fill.fill_history_table())
    return render_template("tables.html", values=values)


@app.route("/bank")
@login_required
def bank():
    """Show portfolio of stocks"""
    if request.method == 'POST':
        json_data = json_decoder(request.get_json())

        if not json_data:
            data = (fill.fill_pc_table())['values']
        else:
            data = fill.db.get_values_with_filter("bank_licences", **json_data)

        return make_response(jsonify(data), 200)

    values = (fill.fill_bank_table())
    return render_template("tables.html", values=values)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        print(rows)
        session["user_id"] = rows[0]["id_users"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template(f"login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        data = db.execute("SELECT username from users")
        data = [elem["username"] for elem in data]

        if not username:
            return apology("Input name")
        elif username in data:
            return apology("This name is already exists")
        elif not password:
            return apology("Input password")
        elif not confirmation:
            return apology("Input confirmation")
        elif password != confirmation:
            return apology("Passwords don't matches")

        hashed_password = generate_password_hash(password)
        db.execute(f"""INSERT INTO users (username, hash) VALUES(?, ?)""", username, hashed_password)

        return render_template(f"register.html")
    else:
        return render_template(f"/register.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
