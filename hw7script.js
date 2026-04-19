const button = document.getElementById("togglebutton");
const box = document.getElementById("box");

function toggleBox() {
    box.classList.toggle("active");
}
button.addEventListener("click", toggleBox);