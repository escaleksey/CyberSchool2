document.addEventListener("DOMContentLoaded", function() {
    let add_button = document.querySelector("#add_button")

    add_button.onclick = function () {
        let window_url = window.location.href.split("/");
        let type = window_url[window_url.length - 1];

        document.location.href = '/add?' + 'type=' + type;
    }
});