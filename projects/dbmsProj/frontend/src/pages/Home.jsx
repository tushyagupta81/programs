import { useEffect } from "react";
import Card from "../components/Card";
import Navbar from "../components/Navbar";
import { useDebouncedCallback } from "use-debounce";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();
  const [price, setPrice] = useState(0);
  const [title, setTitle] = useState("");

  const handleChange = useDebouncedCallback(async () => {
    const getData = async () => {
      let url = `https://apex.oracle.com/pls/apex/tushya/proj/getproperties/?token_=${localStorage.getItem("token")}`;
      if (price > 3) {
        url += `&price=${price}`;
      }
      if (title.length > 0) {
        url += `&title=${title}`;
      }
      console.log(url);
      const res = await fetch(url, {
        method: "GET",
      });
      const obj = await res.json();
      if (obj.status === 401) {
        navigate("/logout");
      }
      console.log(obj);
    };
    getData();
  }, 1000);

  useEffect(() => {
    if (localStorage.getItem("token") == null) {
      navigate("/login");
      return;
    }
    const getData = async () => {
      const url = `https://apex.oracle.com/pls/apex/tushya/proj/getproperties/?token_=${localStorage.getItem("token")}`;
      const res = await fetch(url, {
        method: "GET",
      });
      const obj = await res.json();
      if (obj.status === 401) {
        navigate("/login");
      }
      console.log(obj);
    };
    getData();
  }, [navigate]);
  return (
    <>
      <Navbar />
      <div className="w-[80%] mx-auto flex flex-col py-4 gap-2">
        <span className="flex flex-row gap-2">
          <label htmlFor="Price" className="text-xl">
            Price(max):
          </label>
          <input
            type="number"
            className="border border-black rounded-md"
            value={price}
            onChange={(e) => {
              setPrice(e.target.value);
              handleChange();
            }}
          />
        </span>
        <span className="flex flex-row gap-2">
          <label htmlFor="title" className="text-xl">
            Title:
          </label>
          <input
            type="text"
            className="border border-black rounded-md"
            value={title}
            onChange={(e) => {
              setTitle(e.target.value);
              handleChange();
            }}
          />
        </span>
      </div>
      <div className="grid xl:grid-cols-4 md:grid-cols-2 gap-10 w-[80%] mx-auto">
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
      </div>
    </>
  );
};

export default Home;