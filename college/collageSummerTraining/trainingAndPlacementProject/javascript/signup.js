const login = document.getElementById("login");
const home = document.getElementById("home");
const home_btn = document.getElementById("home-page-btn");
function handler(o) {
  if (o === 1) {
    window.location.href = "login.html";
  } else if (o === 2) {
    window.location.href = "index.html";
  } else if (0 === 3) {
    window.location.href = "index.html";
  }
}
login.addEventListener("click", () => handler(1));
home.addEventListener("click", () => handler(2));
home_btn.addEventListener("click", () => handler(3));

const form_ele = document.getElementById("form-ele");
async function handleLogin(event) {
  event.preventDefault();
  var form = new FormData(event.target);
  for (var pair of form.entries()) {
    console.log(pair[0] + ": " + pair[1]);
  }
  console.log(Object.fromEntries(form));
  const url = "http://localhost:3000/";
  const res = await fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "no-cors",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(Object.fromEntries(form)), // body data type must match "Content-Type" header
  });
  console.log(res);
}
form_ele.addEventListener("submit", (e) => handleLogin(e));
