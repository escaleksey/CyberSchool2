import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from utils.db_functions.db_functions import DataBase


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


def get_table_data(type: str):
    columns = {
        'pc': {
            'IP адрес': {'code': 'local_IP_adress', 'type': 'text'},
            'Версия ОС': {'code': 'OS_version', 'type': 'text'},
            'Видеокарта': {'code': 'video_card', 'type': 'text'},
            'Внешний IP адрес': {'code': 'external_IP_adress', 'type': 'text'},
            'Жесткий диск': {'code': 'hard_disk', 'type': 'text'},
            'Имя пользователя': {'code': 'user_name', 'type': 'text'},
            'Инвентарный номер': {'code': 'item_number', 'type': 'number'},
            'Класс': {'code': 'class_pk', 'type': 'text'},
            'Материнская плата': {'code': 'details', 'type': 'text'},
            'Наличие CD-rom': {'code': 'CD_rom', 'type': 'checkbox'},
            'Наличие внешней сетевой карты': {'code': 'external_network_card', 'type': 'checkbox'},
            'Номер требования': {'code': 'num_of_rec', 'type': 'text'},
            'ОЗУ': {'code': 'amount_of_RAM', 'type': 'text'},
            'ПО': {'code': 'licences', 'type': 'checkbox'},
            'Процессор': {'code': 'processor', 'type': 'text'},
            'Сетевое название': {'code': 'network_name', 'type': 'text'},
            'Тип': {'code': 'type_pk', 'type': 'text'}
        },
        'office_equipment': {
            'Монитор': {'code': 'monitor', 'type': 'number'},
            'Принтер': {'code': 'printer', 'type': 'number'},
            'МФУ': {'code': 'mfu', 'type': 'number'},
            'Сканер': {'code': 'skaner', 'type': 'number'},
            'Ксерокс': {'code': 'xerox', 'type': 'number'},
            'Плоттер': {'code': 'plotter', 'type': 'number'},
            'ИБП': {'code': 'ibp', 'type': 'number'}
        },
        'employees': {
            'ФИО': {'code': 'full_name', 'type': 'text'}, 'ID ПК': {'code': 'id_pk', 'type': 'number'},
            'Полномочия': {'code': 'authority', 'type': 'text'},
            'Дата': {'code': 'date', 'type': 'text'},
            'Состояние': {'code': 'status', 'type': 'text'}
        },
        'bank': {
            'Наименование': {'code': 'name_of_product', 'type': 'text'},
            'Наличие персонализации ': {'code': 'personalization', 'type': 'checkbox'},
            'Вид персонализации': {'code': 'type_of_personalization', 'type': 'text'},
            'Ключ лицензии': {'code': 'personalization_key', 'type': 'text'},
            'Примечание': {'code': 'note', 'type': 'text'}
        },
        'equipment_received': {
            'Дата поступления': {'code': 'date', 'type': 'text'},
            'Фирма поставщик': {'code': 'supplier_firm', 'type': 'text'},
            'Гарантийный срок': {'code': 'guarantee_period', 'type': 'text'},
            'Тип оборудования ': {'code': 'equipment_type', 'type': 'text'},
            'Наименование оборудования': {'code': 'equipment_name', 'type': 'text'},
            'Серийный номер': {'code': 'serial_number', 'type': 'number'},
            'Причина поступления': {'code': 'reason_for_admission', 'type': 'text'},
            'Документ на поступившее оборудование': {'code': 'document', 'type': 'text'},
            'Номер оборудования (присвоенный УИТом)': {'code': 'equipment_number',
                                                       'type': 'number'},
            'Инвентарный номер': {'code': 'item_number', 'type': 'text'},
            'Номер требования': {'code': 'num_of_rec', 'type': 'text'}
        }
    }

    names = {
        "pc": "ПК",
        "office_equipment": "ОФИСНОЕ ОБОРУДОВАНИЕ",
        "employees": "СОТРУДНИКИ",
        "bank": "БАНК ЛИЦЕНЗИЙ",
        "equipment_received": 'ПОЛУЧЕННОЕ ОБОРУДОВАНИЕ'
    }
    return columns[type], names[type]


def get_adding_method(type: str, db: DataBase):
    methods = {
        "pc": db.add_pk,
        "office_equipment": db.add_org_tech,
        "employees": db.add_employee,
        "bank": db.add_bank_licences,
        "equipment_received": db.add_received_equipment
    }

    return methods[type]
