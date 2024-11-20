import { useEffect } from "react";
import Navbar from "../components/Navbar";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import Card from "../components/Card";

const My = () => {
  const navigate = useNavigate();
  const [data, setData] = useState([]);

  useEffect(() => {
    if (localStorage.getItem("token") == null) {
      navigate("/login");
      return;
    }
    const getData = async () => {
      const url = `https://apex.oracle.com/pls/apex/tushya/proj/my/?token_=${localStorage.getItem("token")}`;
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
      <div className="grid xl:grid-cols-4 md:grid-cols-2 gap-10 w-[80%] mx-auto mt-8">
        {data?.map((card_data) => (
          <Card info={card_data} key={card_data.PROPERTY_ID} />
        ))}
      </div>
    </>
  );
};

export default My;
