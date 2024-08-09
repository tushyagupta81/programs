const login = document.getElementById("login");
const signup = document.getElementById("signup");
const home_btn = document.getElementById("home-page-btn");
function handler(o){
    if(o===1){
        window.location.href = "login.html";
    }else if(o===2){
        window.location.href = "signup.html"
    }else if(0===3){
        window.location.href = "index.html";
    }
}
login.addEventListener('click',() => handler(1));
signup.addEventListener('click',() => handler(2));
home_btn.addEventListener('click', () => handler(3));

console.log("Panjab University");
window.alert("Punjab University");


const form_ele = document.getElementById("form-ele");
function handleLogin(event) {
  event.preventDefault();
  var form = new FormData(event.target);
  let obj = Object.fromEntries(form) 
  let max = Number(obj['n1']);
  if(max<Number(obj['n2'])){
    max = Number(obj['n2']);
  }
  console.log(`bigger number is ${max}`);
}
form_ele.addEventListener("submit", (e) => handleLogin(e));
