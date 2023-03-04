from utils.db_functions.db_functions import DataBase


class FillTable():
    def __init__(self, db):
        self.db = DataBase(db)

    def fill_pc_table(self):
        data = self.db.get_all_values_pk()
        titles = ['ID', 'Тип', 'Класс', 'Материнская плата', 'ОЗУ', 'Жесткий диск', 'Видеокарта', 'Процессор',
                  'Наличие CD-rom', 'Наличие внешней сетевой карты', 'Версия ОС', 'ПО', 'Инвентарный номер',
                  'Сетевое название', 'Имя пользователя', 'IP адрес', 'Внешний IP адрес',
                  'Номер требования']

        values = [[elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7],
                   elem[8], elem[9], elem[10], elem[13], elem[15], elem[16], elem[17], elem[18],
                   elem[21], elem[22]] for elem in data]
        result = {'name': 'ПК', 'titles': titles, 'values': values}
        return result

    def fill_equipment_received_table(self):
        data = self.db.get_all_values_equipment_received()
        titles = ['ID', 'Дата поступления', 'Фирма поставщик', 'Гарантийный срок', 'Тип оборудования ',
                  'Наименование оборудования', 'Серийный номер', 'Причина поступления',
                  'Документ на поступившее оборудование', 'Номер оборудования (присвоенный УИТом)',
                  'Инвентарный номер', 'Номер требования']

        values = [list(elem) for elem in data]

        result = {'name': 'ПОЛУЧЕННОЕ ОБОРУДОВАНИЕ', 'titles': titles, 'values': values}
        return result

    def fill_office_equipment_table(self):
        data = self.db.get_all_values_org_tech()
        titles = ['ID', 'Монитор', 'Принтер', 'МФУ', 'Сканер', 'Ксерокс', 'Плоттер', 'ИБП']

        values = [list(elem) for elem in data]

        result = {'name': 'ОРГТЕХНИКА', 'titles': titles, 'values': values}
        return result

    def fill_employees_table(self):
        data = self.db.get_all_values_employee()
        titles = ['ID', 'ФИО', 'ID ПК', 'Полномочия', 'Дата', 'Состояние']

        values = [list(elem) for elem in data]

        result = {'name': 'СОТРУДНИКИ', 'titles': titles, 'values': values}
        return result


    def fill_cards_table(self):
        result = {'name': 'КАРТОЧКИ', 'titles': [], 'values': [[]]}
        return result

    def fill_history_table(self):
        result = {'name': 'ИСТОРИЯ', 'titles': [], 'values': [[]]}
        return result

    def fill_bank_table(self):
        data = self.db.get_all_values_bank()
        titles = ['ID', 'Наименование', 'Наличие персонализации ', 'Вид персонализации', 'Ключ лицензии', 'Примечание']

        values = [list(elem) for elem in data]

        result = {'name': 'ПК', 'titles': titles, 'values': values}
        return result
