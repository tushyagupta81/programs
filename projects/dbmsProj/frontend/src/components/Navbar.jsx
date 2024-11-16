import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="flex flex-row justify-between bg-blue-200 h-12 items-center px-6">
      <Link to="/">DBMS Project</Link>
      <div className="flex gap-4">
        <span>Create listing</span>
        <Link to="/login">Login</Link>
        <span>Logout</span>
      </div>
    </div>
  );
};

export default Navbar;
