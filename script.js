const myArray = ['Apple', 'Banana', 'Cherry', 'Date', 'Berry'];

const container = document.querySelector('#array-container');

for (let i = 0; i < myArray.length; i++) {
    const p = document.createElement('p')


    p.textContent = myArray[i];
    container.appendChild(p);
}