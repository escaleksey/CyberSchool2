const convector = {
    "pc": {
        "ID": "id_pk",
        "IP_адрес": "local_IP_adress",
        "Версия_ОС": "OS_version",
        "Видеокарта": "video_card",
        "Внешний_IP_адрес": "external_IP_adress",
        "Жесткий_диск": "hard_disk",
        "Имя_пользователя": "user_name",
        "Инвентарный_номер": "item_number",
        "Класс": "class_pk",
        "Материнская_плата": "details",
        "Наличие_CD-rom": "CD_rom",
        "Наличие_внешней_сетевой_карты": "external_network_card",
        "Номер_требования": "num_of_rec",
        "ОЗУ": "amount_of_RAM",
        "ПО": "licences",
        "Процессор": "processor",
        "Сетевое_название": "network_name",
        "Тип": "type_pk"
    },
    "office_equipment": {
        "ID": "type_org",
        "Монитор": "monitor",
        "Принтер": "printer",
        "МФУ": "mfu",
        "Сканер": "skaner",
        "Ксерокс": "xerox",
        "Плоттер": "plotter",
        "ИБП": "ibp"
    },
    "employees": {
        "ID": "employee_id",
        "ФИО": "full_name",
        "ID_ПК": "id_pk",
        "Полномочия": "authority",
        "Дата": "date",
        "Состояние": "status"
    },
    "bank": {
        "ID": "id_licences",
        "Наименование": "name_of_product",
        "Наличие_персонализации_": "personalization",
        "Вид_персонализации": "type_of_personalization",
        "Ключ_лицензии": "personalization_key",
        "Примечание": "note"
    },
    "equipment_received": {
        "ID": "equipment_id",
        "Дата_поступления": "date",
        "Фирма_поставщик": "supplier_firm",
        "Гарантийный_срок": "guarantee_period",
        "Тип_оборудования_": "equipment_type",
        "Наименование_оборудования": "equipment_name",
        "Серийный_номер": "serial_number",
        "Причина_поступления": "reason_for_admission",
        "Документ_на_поступившее_оборудование": "document",
        "Номер_оборудования_(присвоенный_УИТом)": "equipment_number",
        "Инвентарный_номер": "item_number",
        "Номер_требования": "num_of_rec"
    }

}

export default convector