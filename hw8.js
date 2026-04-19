const students = ["James","Ben","Ashley","Jacob","Nathan","Becky"];

const button = document.querySelector("#showStudentsbutton");
const container = document.querySelector("#studentContainer");

button.addEventListener("click", function() {
    for (let i=0; i<students.length; i++) {
        const studentElement = document.createElement("p");
        studentElement.textContent = students[i];
        container.appendChild(studentElement);
        if (i % 2 ==0) {
            studentElement.classList.add("red");
        } else {
            studentElement.classList.add("blue");
        }
    }
    
})
