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
import EditListing from "./pages/EditListing.jsx";
import My from "./pages/My.jsx";
import Trans from "./pages/Trans.jsx";
import OneTrans from "./pages/OneTrans.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/transactions" element={<Trans />} />
        <Route path="/transaction/:id" element={<OneTrans />} />
        <Route path="/listing/:id" element={<Listing />} />
        <Route path="/editlisting/:id" element={<EditListing />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/my" element={<My />} />
        <Route path="/create" element={<Create />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
);
