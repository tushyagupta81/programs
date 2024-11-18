import Navbar from "../components/Navbar";

const Create = () => {
  return (
    <>
      <Navbar />
      <div className="w-full h-screen flex items-center justify-center">
        <div className="border border-black shadow-xl rounded-md w-96 py-4">
          <h1 className="w-min mx-auto font-bold text-2xl">Login</h1>
          <form className="flex flex-col gap-2 px-4">
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

export default Create;
