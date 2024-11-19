import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./index.css";
import Home from "./pages/Home.jsx";
import Login from "./pages/Login.jsx";
import Logout from "./pages/Logout.jsx";
import Create from "./pages/Create.jsx";
import Signup from "./pages/Signup.jsx";
import Listing from "./pages/Listing.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/listing/:id" element={<Listing />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/create" element={<Create />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
);
