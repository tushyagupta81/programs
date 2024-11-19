import Navbar from "../components/Navbar";
import { jwtDecode } from "jwt-decode";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();
  const handleSubmit = async (e) => {
    e.preventDefault();
    const email = e.target[0].value;
    const password = e.target[1].value;
    console.log(email, password);
    const res = await fetch(
      "https://apex.oracle.com/pls/apex/tushya/proj/login/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email_: email,
          pwd: password,
        }),
      },
    );
    const obj = await res.json();
    if (obj.status === 200) {
      const decoded = jwtDecode(obj.data);
      localStorage.setItem("token", obj.data);
      localStorage.setItem("role", decoded.role);
      console.log(decoded);
      navigate("/");
    } else if (obj.status === 404) {
      e.target[1].value = "";
      alert("Username or password does not exist");
    } else if (obj.status === 401) {
      e.target[1].value = "";
      alert("Wrong password");
    }
  };
  return (
    <>
      <Navbar />
      <div className="w-full h-screen flex items-center justify-center">
        <div className="border border-black shadow-xl rounded-md w-96 py-4">
          <h1 className="w-min mx-auto font-bold text-2xl">Login</h1>
          <form className="flex flex-col gap-2 px-4" onSubmit={handleSubmit}>
            <label htmlFor="email">Email</label>
            <input
              type="text"
              name="email"
              className="border border-black rounded-md h-8 pl-2"
              required
            />
            <label htmlFor="password">Password</label>
            <input
              type="password"
              name="password"
              minLength={8}
              className="border border-black rounded-md h-8 pl-2"
              required
            />
            <input
              type="submit"
              value="Submit"
              className="border border-black rounded-full w-min px-4 py-2 mx-auto bg-green-300 mt-2"
            />
          </form>
        </div>
      </div>
    </>
  );
};

export default Login;
