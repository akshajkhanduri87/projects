for (let i = 1; i <= 3; i++) {
    const h1 = document.createElement("h1");
    h1.textContent = `This is H1 number ${i}`;
    document.getElementById("container").appendChild(h1);
}