const f = document.getElementById("form");
f.addEventListener("submit", (e) => handleSubmit(e));

const username = "Tushya";
const password = "123";

function handleSubmit(e) {
  e.preventDefault();
  const u = e.target[0].value;
  const p = e.target[1].value;
  if (u === "" && p === "") {
    alert("Please fill all the fields");
    return;
  } else if (p === "") {
    alert("Please fill password field");
    return;
  } else if (u === "") {
    alert("Please fill username field");
    return;
  }
  if (u === username && p === password) {
    alert("Welcome");
  } else {
    alert("Please enter valid username and password");
  }
}
