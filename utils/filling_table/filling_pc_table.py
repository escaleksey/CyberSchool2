from utils.db_functions.db_functions import DataBase


def fill_pc_table(db):
    data_base = DataBase(db)
    data = data_base.get_all_values_pk()
    titles = ['ID', 'Тип', 'Класс', 'Материнская плата', 'ОЗУ', 'Жесткий диск', 'Видеокарта', 'Процессор',
              'Наличие CD-rom', 'Наличие внешней сетевой карты', 'Версия ОС', 'ПО', 'Инвентарный номер',
              'Сетевое название', 'Имя пользователя', 'IP адрес', 'Внешний IP адрес',
              'Номер требования']

    values = [[elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7],
               elem[8], elem[9], elem[10], elem[13], elem[15], elem[16], elem[17], elem[18],
               elem[21], elem[22]] for elem in data]
    result = {'name': 'ПК', 'titles': titles, 'values': values}
    return result


if __name__ == '__main__':
    print(fill_pc_table())