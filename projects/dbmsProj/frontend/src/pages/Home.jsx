import { useEffect } from "react";
import Card from "../components/Card";
import Navbar from "../components/Navbar";
import { useDebouncedCallback } from "use-debounce";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();
  const [data, setData] = useState([]);
  const [price, setPrice] = useState();
  const [city, setCity] = useState("");

  const handleChange = useDebouncedCallback(async () => {
    const getData = async () => {
      let url = `https://apex.oracle.com/pls/apex/tushya/proj/getproperties/?token_=${localStorage.getItem("token")}`;
      if (price > 3) {
        url += `&price=${price}`;
      }
      if (city.length > 0) {
        url += `&city=${city}`;
      }
      const res = await fetch(url, {
        method: "GET",
      });
      const obj = await res.json();
      if (obj.status === 401) {
        navigate("/logout");
      }
      setData(obj.data);
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
        navigate("/logout");
      }
      setData(obj.data);
    };
    getData();
  }, [navigate]);
  return (
    <>
      <Navbar />
      <div className="w-[80%] mx-auto flex flex-row py-4 gap-4 my-4">
        <span className="flex flex-row gap-2">
          <input
            type="number"
            className="border-b-2 border-gray-400 bg-white pl-2 h-8 w-64"
            value={price}
            placeholder="Price(max)"
            onChange={(e) => {
              setPrice(e.target.value);
              handleChange();
            }}
          />
        </span>
        <span className="flex flex-row gap-2">
          <input
            type="text"
            className="border-b-2 border-gray-400 bg-white pl-2 h-8 w-64"
            name="city"
            placeholder="City"
            value={city}
            onChange={(e) => {
              setCity(e.target.value);
              handleChange();
            }}
          />
        </span>
      </div>
      <div className="grid xl:grid-cols-4 md:grid-cols-2 gap-10 w-[80%] mx-auto">
        {data?.map((card_data) => (
          <Card info={card_data} key={card_data.PROPERTY_ID} />
        ))}
      </div>
    </>
  );
};

export default Home;
