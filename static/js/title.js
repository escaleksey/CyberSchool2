function func() {
    var c = document.getElementById('checkboxes').getElementsByTagName('input').length;
    console.log(c);
    for (let i = 1; i < c + 1; i++) {
        var z = String(i) + "_check";
        var x = String(i) + "_model_container";
        if (document.getElementById(z).checked) {
            document.getElementById(x).classList.remove('false');
        }
        else {
            document.getElementById(x).classList.add('false');
        }
    };
}