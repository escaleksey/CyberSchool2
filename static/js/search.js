document.addEventListener("DOMContentLoaded", function() {
    let search_button = document.querySelector("#search_button");

    search_button.onclick = function() {
        let table = document.getElementById("table-view");
        for (let row of table.rows) {
            alert(row);
        }
    }
});