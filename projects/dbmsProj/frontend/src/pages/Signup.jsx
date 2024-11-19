import Navbar from "../components/Navbar";

const Signup = () => {
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(e);
    const username = e.target[0].value;
    const password = e.target[1].value;
    const phone = e.target[2].value;
    const role = e.target[3].value;
    console.log(username, password, phone, role);
    const res = await fetch(
      "https://apex.oracle.com/pls/apex/tushya/proj/login/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          userName: uname,
          pwd: password,
        }),
      },
    );
    const obj = await res.json();
    if (obj.status === 200) {
      const decoded = jwtDecode(obj.data);
      localStorage.setItem("token", obj.data);
      localStorage.setItem("role", decoded.job);
      console.log(decoded);
      navigate("/");
    } else {
      e.target[1].value = "";
      alert("Username or password does not exist");
    }
  };
  return (
    <>
      <Navbar />
      <div className="w-full h-screen flex items-center justify-center">
        <div className="border border-black shadow-xl rounded-md w-96 py-4">
          <h1 className="w-min mx-auto font-bold text-2xl">Signup</h1>
          <form className="flex flex-col gap-2 px-4" onSubmit={handleSubmit}>
            <label htmlFor="username">Username</label>
            <input
              type="text"
              name="username"
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
            <label htmlFor="phone">Phone number</label>
            <input
              type="number"
              min={1000000000}
              max={9999999999}
              className="border border-black rounded-md h-8 px-2"
              required
            />
            <label htmlFor="role">Role</label>
            <select
              name="role"
              id="role"
              className="border blorder-black h-8 rounded-md pl-2"
            >
              <option value="client">Client</option>
              <option value="agent">Agent</option>
            </select>
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

export default Signup;
