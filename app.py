from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from utils.helpers import apology, login_required
from utils.filling_table.filling_pc_table import fill_pc_table

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
    stocks, cash, summa = [{"symbol": '2', "name": '123', "count": '1', "price":'23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price":'23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price":'23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price":'23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price":'23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price":'23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price":'23', "total": '23'},
                           {"symbol": '2', "name": '123', "count": '1', "price": '23', "total": '23'}], 0, 0

    return render_template(f"index.html", stocks=stocks, cash=cash, summa=summa)


@app.route("/pc")
@login_required
def pc():
    """Show portfolio of stocks"""
    values = (fill_pc_table("static/db/database.db"))
    return render_template("tables.html", values=values)


@app.route("/equipment_received")
@login_required
def equipment_received():
    """Show portfolio of stocks"""
    values = (fill_pc_table("static/db/database.db"))
    return render_template("tables.html", values=values)


@app.route("/office_equipment")
@login_required
def office_equipment():
    """Show portfolio of stocks"""
    values = (fill_pc_table("static/db/database.db"))
    return render_template("tables.html", values=values)


@app.route("/employees")
@login_required
def employees():
    """Show portfolio of stocks"""
    values = (fill_pc_table("static/db/database.db"))
    return render_template("tables.html", values=values)


@app.route("/cards")
@login_required
def cards():
    """Show portfolio of stocks"""
    values = (fill_pc_table("static/db/database.db"))
    return render_template("tables.html", values=values)


@app.route("/history")
@login_required
def history():
    """Show portfolio of stocks"""
    values = (fill_pc_table("static/db/database.db"))
    return render_template("tables.html", values=values)

@app.route("/bank")
@login_required
def bank():
    """Show portfolio of stocks"""
    values = (fill_pc_table("static/db/database.db"))
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
        session["user_id"] = rows[0]["id"]

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
        session["user_id"] = username
        return redirect('/')
    else:
        return render_template(f"register.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
