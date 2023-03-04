import sqlite3


class ErrorCertificate(Exception):
    pass


class DataBase:
    """
    Класс для работы с базой данных
    """
    def add_employee(self, dict_of_value: dict) -> bool:
        """
        :param dict_of_value
        :return: None
        добавляет сертификат в бд
        """
        list_of_value = list(dict_of_value.values())

        cur = self.con.cursor()
        request = f'''INSERT OR IGNORE INTO employee(employee_id, full_name, post, id_pk, authority, status, date)
         VALUES({list_of_value[0]}, "{list_of_value[1]}", "{list_of_value[2]}", {list_of_value[3]},
          "{list_of_value[4]}", "{list_of_value[5]}", "{list_of_value[6]}");'''

        cur.execute(request)
        self.con.commit()
        cur.close()
        return 1

    def add_pk(self, dict_of_value: dict) -> bool:
        """
        :param dict_of_value
        :return: None
        добавляет сертификат в бд
        """
        list_of_value = list(dict_of_value.values())

        cur = self.con.cursor()
        request = f'''INSERT OR IGNORE INTO pk(id_pk, type_pk, class_pk, details, amount_of_RAM, hard_disk,
        video_card, processor, CD_rom, external_network_card, OS_version, licences, licence_key, software, 
        personalization, item_number, network_name, user_name, local_IP_adress, local_inet_availability,
        external_inet_availability, external_IP_adress, num_of_rec) 
        VALUES({list_of_value[0]}, "{list_of_value[1]}", "{list_of_value[2]}", "{list_of_value[3]}",
        "{list_of_value[4]}", "{list_of_value[5]}", "{list_of_value[6]}", "{list_of_value[7]}", {list_of_value[8]},
        {list_of_value[9]}, "{list_of_value[10]}", {list_of_value[11]}, "{list_of_value[12]}", "{list_of_value[13]}",
        "{list_of_value[14]}", {list_of_value[15]},"{list_of_value[16]}", "{list_of_value[17]}", "{list_of_value[18]}",
         {list_of_value[19]}, {list_of_value[20]}, {list_of_value[21]}, "{list_of_value[22]}");'''

        cur.execute(request)
        self.con.commit()
        cur.close()
        return 1

    def get_all_values_pk(self):
        cur = self.con.cursor()

        try:
            cur.execute(f"SELECT * FROM pk")
            return list(cur.fetchall())
        finally:
            cur.close()
