import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from utils.filling_table.filling_table import FillTable


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def get_table_data(fill: FillTable, type: str):
    tables = {
        'pc': fill.fill_pc_table,
        'office_equipment': fill.fill_office_equipment_table,
        'employees': fill.fill_employees_table,
        'bank': fill.fill_bank_table,
        'equipment_received': fill.fill_equipment_received_table,
    }

    return tables[type]()