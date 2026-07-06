const search = document.getElementById("search");
const select = document.getElementById("movieSelect");

search.addEventListener("keyup", function () {

    let filter = search.value.toLowerCase();

    for (let option of select.options) {

        let txt = option.text.toLowerCase();

        option.hidden = !txt.includes(filter);

    }

});