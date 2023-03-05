document.addEventListener("DOMContentLoaded", function () {

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
            "ID": "id_org_tech",
            "Тип_оргтехники": "type_org",
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

    function resetTable(data) {

        let elements = document.querySelectorAll('#row');
        for (let elem of elements) {
            elem.parentNode.removeChild(elem);
        }

        let tbody = document.getElementById("tbody")

        for (let elem of data) {

            let tr = document.createElement('tr');
            tr.setAttribute('id', 'row');

            let td = document.createElement('td');
            td.setAttribute('class', 'text-center');
            tr.appendChild(td)

            for (let elemItem of elem) {
                let td = document.createElement('td');
                td.innerText = elemItem;
                tr.appendChild(td)
            }
            tbody.appendChild(tr)
        }
    }


    let window_url = window.location.href.split("/")
    let type = window_url[window_url.length - 1]


    document.querySelector("#search_button").onclick = function () {
        let jsonData = {}
        let elements = document.querySelectorAll('.search');
        for (let elem of elements) {
            console.log(elem)
            jsonData[convector[type][elem.name]] = elem.value
        }
        console.log(type)
        console.log(jsonData)
        fetch(
            "/" + type,
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                method: "POST",
                body: JSON.stringify(jsonData)
            })
            .then((response) => response.json()) //2
            .then((data) => {
                resetTable(data)
                console.log(data); //3
            })
            .catch(function (res) {
                    console.log(res)
                }
            )
    }


});