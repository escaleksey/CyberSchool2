document.addEventListener("DOMContentLoaded", function () {

    let convector = {
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
        }
    }


    let search_button = document.querySelector("#search_button");

    search_button.onclick = function () {
        let jsonData = {}
        let elements = document.querySelectorAll('.search');
        for (let elem of elements) {
            jsonData[elem.name] = elem.value
        }
        console.log(jsonData)
    }
});