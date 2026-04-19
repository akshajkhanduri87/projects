const button = document.querySelector("#myButton");

function eventButtonFunc() {
	console.log("clicked the button");
}

button.addEventListener("click", eventButtonFunc);