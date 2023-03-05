import sqlite3

from __config__ import PROJECT_PATH

conn = sqlite3.connect(f'{PROJECT_PATH}/static/db/database.db')
cur = conn.cursor()

# create tables
cur.execute("""CREATE TABLE bank_licences (
    id_licences             INTEGER PRIMARY KEY AUTOINCREMENT
                                    UNIQUE
                                    NOT NULL,
    name_of_product         TEXT,
    personalization         BOOLEAN DEFAULT (False),
    type_of_personalization TEXT    CHECK (personalization == True),
    personalization_key     TEXT    NOT NULL,
    note                    TEXT
);
""")

cur.execute("""CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT
                        UNIQUE
                        NOT NULL,
    full_name   TEXT    NOT NULL,
    post        TEXT    NOT NULL,
    id_pk       INT,
    authority   TEXT,
    status      TEXT,
    date        TEXT    NOT NULL
);
""")

cur.execute("""CREATE TABLE equipment_received (
    equipment_id         INTEGER PRIMARY KEY AUTOINCREMENT
                                 UNIQUE,
    date                 TEXT,
    supplier_firm        TEXT,
    guarantee_period     TEXT    NOT NULL,
    equipment_type       TEXT,
    equipment_name       TEXT,
    serial_number        INT,
    reason_for_admission TEXT,
    document             TEXT,
    equipment_number     INT     UNIQUE,
    item_number          TEXT,
    num_of_rec           TEXT
);
""")

cur.execute("""CREATE TABLE card (
    id_card     INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pk       INT,
    id_employee INT,
    structure   TEXT,
    corpus      TEXT,
    room_number TEXT,
    id_org_tech TEXT,
    data        TEXT
);
""")

cur.execute("""CREATE TABLE org_tech (
    id_org_tech                 INTEGER PRIMARY KEY AUTOINCREMENT,
    type_org TEXT 
);
""")

cur.execute("""CREATE TABLE pk (
    id_pk                      INTEGER PRIMARY KEY AUTOINCREMENT,
    type_pk                    TEXT,
    class_pk                   TEXT,
    details                    TEXT,
    amount_of_RAM              TEXT,
    hard_disk                  TEXT,
    video_card                 TEXT,
    processor                  TEXT,
    CD_rom                     BOOLEAN DEFAULT (False),
    external_network_card      BOOLEAN DEFAULT (False),
    OS_version                 TEXT,
    licences                   BOOLEAN DEFAULT (False),
    licence_key                TEXT,
    software                   TEXT,
    personalization            TEXT,
    item_number                INT     UNIQUE,
    network_name               TEXT,
    user_name                  TEXT,
    local_IP_adress            TEXT,
    local_inet_availability    BOOLEAN DEFAULT (False),
    external_inet_availability BOOLEAN DEFAULT (False),
    external_IP_adress         INT     DEFAULT None,
    num_of_rec                 TEXT
);
""")

cur.execute("""CREATE TABLE users (
    id_users INTEGER PRIMARY KEY AUTOINCREMENT
                     UNIQUE
                     NOT NULL,
    username         NOT NULL,
    hash     STRING  NOT NULL
);
""")

cur.execute(f'''INSERT OR IGNORE INTO org_tech(id_org_tech, type_org)
         VALUES({1}, "Монитор");''')

cur.execute(f'''INSERT OR IGNORE INTO org_tech(id_org_tech, type_org)
         VALUES({2}, "Принтер");''')
cur.execute(f'''INSERT OR IGNORE INTO org_tech(id_org_tech, type_org)
         VALUES({3}, "МФУ");''')
cur.execute(f'''INSERT OR IGNORE INTO org_tech(id_org_tech, type_org)
         VALUES({4}, "Сканер");''')
cur.execute(f'''INSERT OR IGNORE INTO org_tech(id_org_tech, type_org)
         VALUES({5}, "Ксерокс");''')
cur.execute(f'''INSERT OR IGNORE INTO org_tech(id_org_tech, type_org)
         VALUES({6}, "Плоттер");''')
cur.execute(f'''INSERT OR IGNORE INTO org_tech(id_org_tech, type_org)
         VALUES({7}, "ИБП");''')

conn.commit()



