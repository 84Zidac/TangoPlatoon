const showGreeting = () => {
  let nameInput = document.getElementById("input-name");
  let greetingOutput = document.getElementById("output");
  if (nameInput && greetingOutput) {
    greetingOutput.innerHTML = "Hello " + nameInput.value + "!";
  }
};
const updateColor = (color) => {
    let elem = document.getElementById("one"); // will return the [*first*] element that has an id equal to 'one'
    if (elem) {
      elem.style.color = color;
    }
  };