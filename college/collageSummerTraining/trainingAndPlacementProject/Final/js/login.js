const login_form_ele = document.getElementById("login-form");
const signup_form_ele = document.getElementById("signup-form");
async function handleLogin(event) {
  event.preventDefault();
  var form = new FormData(event.target);
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
login_form_ele.addEventListener("submit", (e) => handleLogin(e));
signup_form_ele.addEventListener("submit", (e) => handleLogin(e));
