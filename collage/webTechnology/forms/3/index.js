const form = document.getElementsByTagName("form")[0];
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const username = e.target[0];
  const email = e.target[1];
  const male = e.target[2].checked;
  const female = e.target[3].checked;
  const dob = e.target[4];
  const emp = [username, email, dob];
  for (let v in emp) {
    if (emp[v].value == "") {
      alert(`Please fill out the ${emp[v].name}`);
      return;
    }
  }
  if (username.value.length > 30) {
    alert("username length cannot be greater than 30");
    return;
  }
  if (!(email.value.includes("@") && email.value.includes("."))) {
    alert("Email must include @ and .");
    return;
  }
  if (email.value.length > 30) {
    alert("email length cannot be greater than 30");
    return;
  }
  const day = parseInt(dob.value.split("-")[2]);
  const month = parseInt(dob.value.split("-")[1]);
  const year = parseInt(dob.value.split("-")[0]);
  if (day > 31 || day < 1) {
    alert("Day can be between 1 and 31 only");
    return;
  }
  if (month > 12 || month < 1) {
    alert("Month can be between 1 and 12 only");
    return;
  }
  if (year > 2024 || year < 1900) {
    alert("Year can be between 1900 and 2024 only");
    return;
  }
  if (!(male || female)) {
    alert("Please enter sex");
    return;
  }
});
