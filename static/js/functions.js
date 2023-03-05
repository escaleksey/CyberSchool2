function resetTable(data) {

    let elements = document.querySelectorAll('#row');
    for (let elem of elements) {
        elem.parentNode.removeChild(elem);
    }

    let tbody = document.getElementById("tbody")

    for (let elem of data) {

        let tr = document.createElement('tr');
        tr.setAttribute('id', 'row');

        for (let elemItem of elem) {
            let td = document.createElement('td');
            td.innerText = elemItem;
            tr.appendChild(td)
        }

        console.log(tr)
        tbody.appendChild(tr)
    }
}

export default resetTable
