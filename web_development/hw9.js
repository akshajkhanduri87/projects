const students = ["James", "Ben", "Ashley", "Jacob", "Nathan", "Becky"]

const btnA = document.getElementById("btnA");
const btnB = document.getElementById("btnB");
const container = document.getElementById("studentContainer");

btnA.addEventListener("click",function() {
    container.innerHTML = "";

    for (let i=0;i<students.length;i++) {
    const p = document.createElement("p");
    p.textContent = students[i]
    container.appendChild(p);
    }
});

btnB.addEventListener("click", function() {
    const names = container.querySelectorAll("p");
    for (let i=0;i<names.length;i++) {
        names[i].classList.toggle("colored");
    }


});