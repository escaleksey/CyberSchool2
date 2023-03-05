import random

from __config__ import PROJECT_PATH
from utils.db_functions.db_functions import DataBase


def create_random_str(n=10):
    symbols = 'qwertyuioplkkjhgfdsazxcvbnm'
    return ''.join(random.choices(symbols, k=n))


def create_random_bool():
    return random.choice((True, False))


def create_random_int(n=255):
    return random.randint(0, n)


def generate_rows(data):
    row = {}
    for key, value in data.items():
        match value:
            case 'str':
                row[key] = create_random_str(10)
            case 'bool':
                row[key] = create_random_bool()
            case 'int':
                row[key] = create_random_int(32)
    return row


"""PC"""


def generate_pc_rows(n):
    data = {
        'type_pk': 'str', 'class_pk': 'str', 'details': 'str', 'amount_of_RAM': 'str',
        'hard_disk': 'str', 'video_card': 'str', 'processor': 'str',
        'CD_rom': 'bool', 'external_network_card': 'bool', 'OS_version': 'str',
        'licences': 'bool', 'licence_key': 'str', 'software': 'str',
        'personalization': 'str', 'item_number': 'int', 'network_name': 'str',
        'user_name': 'str', 'local_IP_adress': 'str', 'local_inet_availability': 'bool',
        'external_inet_availability': 'bool', 'external_IP_adress': 'int', 'num_of_rec': 'str'
    }

    for _ in range(n):
        yield generate_rows(data)


def fill_pc_table(n=25):
    print("start filling pc table of database")
    db = DataBase(f'{PROJECT_PATH}/static/db/database.db')
    data = generate_pc_rows(n)

    for row in data:
        db.add_pk(row)
    print("end filling pc table of database")


"""ORG TECH"""


def generate_org_tech_rows(n):
    data = {
        'type_org': 'str',
        'monitor': 'int',
        'printer': 'int',
        'mfu': 'int',
        'skaner': 'int',
        'xerox': 'int',
        'plotter': 'int',
        'ibp': 'int'
    }

    for _ in range(n):
        yield generate_rows(data)


def fill_org_tech_table(n=25):
    db = DataBase(f'{PROJECT_PATH}/static/db/database.db')
    data = generate_org_tech_rows(n)

    for row in data:
        db.add_org_tech(row)


"""EMPLOYERS"""


def generate_employee_rows(n):
    data = {
        'full_name': 'str',
        'post': 'str',
        'id_pk': 'int',
        'authority': 'str',
        'status': 'str',
        'date': 'str'
    }

    for _ in range(n):
        yield generate_rows(data)


def fill_employee_table(n=25):
    print("start filling employee table of database")
    db = DataBase(f'{PROJECT_PATH}/static/db/database.db')
    data = generate_employee_rows(n)

    for row in data:
        db.add_employee(row)
    print("end filling employee table of database")



