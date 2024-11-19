import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="flex flex-row justify-between bg-blue-200 h-12 items-center px-6">
      <Link to="/">DBMS Project</Link>
      <div className="flex gap-4">
        {localStorage.getItem("token") ? (
          <>
            {localStorage.getItem("role") === "agent" && (
              <Link to="/create">Create listing</Link>
            )}
            <Link to="/logout">Logout</Link>
          </>
        ) : (
          <>
            <Link to="/login">Login</Link>
            <Link to="/signup">Signup</Link>
          </>
        )}
      </div>
    </div>
  );
};

export default Navbar;
