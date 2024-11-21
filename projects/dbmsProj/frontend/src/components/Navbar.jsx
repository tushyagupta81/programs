import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="flex flex-row justify-between bg-blue-200 h-12 items-center px-6">
      <Link
        to="/"
        className="hover:bg-blue-300 rounded-md py-1 px-2 text-xl font-bold hover:scale-105 transform transition duration-75"
      >
        DBMS Project
      </Link>
      <div className="flex gap-2">
        {localStorage.getItem("token") ? (
          <>
            {localStorage.getItem("role") === "agent" && (
              <>
                <Link
                  to="/create"
                  className="hover:bg-blue-300 rounded-md py-1 px-2 hover:scale-110 transform transition duration-75"
                >
                  Create listing
                </Link>
                <Link
                  to="/my"
                  className="hover:bg-blue-300 rounded-md py-1 px-2 hover:scale-110 transform transition duration-75"
                >
                  View My Listings
                </Link>
              </>
            )}
            <Link
              to="/transactions"
              className="hover:bg-blue-300 rounded-md py-1 px-2 hover:scale-110 transform transition duration-75"
            >
              My transactions
            </Link>
            <Link
              to="/logout"
              className="hover:bg-blue-300 rounded-md py-1 px-2 hover:scale-110 transform transition duration-75"
            >
              Logout
            </Link>
          </>
        ) : (
          <>
            <Link
              to="/login"
              className="hover:bg-blue-300 rounded-md py-1 px-2 hover:scale-110 transform transition duration-75"
            >
              Login
            </Link>
            <Link
              to="/signup"
              className="hover:bg-blue-300 rounded-md py-1 px-2 hover:scale-110 transform transition duration-75"
            >
              Signup
            </Link>
          </>
        )}
      </div>
    </div>
  );
};

export default Navbar;
