import convector from "./consts";
import resetTable from "./functions";

document.addEventListener("DOMContentLoaded", function () {

    let window_url = window.location.href.split("/")
    let type = window_url[window_url.length - 1]

    let search_button = document.querySelector("#search_button");

    search_button.onclick = function () {
        let jsonData = {}
        let elements = document.querySelectorAll('.search');
        for (let elem of elements) {
            jsonData[convector[type][elem.name]] = encodeURIComponent(elem.value)
        }
        console.log(jsonData)
        fetch(
            "/pc",
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