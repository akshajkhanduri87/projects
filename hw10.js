const students = ["James", "Ben", "Ashley", "Jacob", "Nathan", "Becky"];

const btnA = document.getElementById("btnA");
const btnB = document.getElementById("btnB");
const btnC = document.getElementById("btnC");

const container = document.getElementById("studentContainer");
const statusText = document.getElementById("statusText");


btnA.addEventListener("click", function() {

    container.innerHTML = "";

    for (let i = 0; i < students.length; i++) {

        const student = document.createElement("div");
        student.textContent = students[i];

        container.appendChild(student);
    }

    statusText.textContent = "Showing " + students.length + " students";
});

btnB.addEventListener("click", function() {
    const studentList = container.querySelectorAll("div");

    for(let i=0;i<studentList.length;i++) {
        studentList[i].classList.toggle("highlight");
    }
});

btnC.addEventListener("click", function() {
    container.innerHTML = "";
    for(let i= students.length-1;i>=0;i--) {
        const studentDiv = document.createElement("div")
        studentDiv.textContent = students[i];
        container.appendChild(studentDiv);
    }
    statusText.textContent = "Showing " + students.length + " students in reverse";

})