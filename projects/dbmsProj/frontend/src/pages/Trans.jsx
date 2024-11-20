import { useEffect } from "react";
import Navbar from "../components/Navbar";
import { useState } from "react";
import TransCard from "../components/TransCard";
import { useNavigate } from "react-router-dom";

const Trans = () => {
  const navigate = useNavigate();
  const [data, setData] = useState();
  useEffect(() => {
    const getData = async () => {
      const url = `https://apex.oracle.com/pls/apex/tushya/proj/gettransactions/?token_=${localStorage.getItem("token")}`;
      const res = await fetch(url, {
        method: "GET",
      });
      const obj = await res.json();
      if (obj.status === 401) {
        navigate("/logout");
      }
      setData(obj);
    };
    getData();
  }, [navigate]);
  return (
    <>
      <Navbar />
      <div className="w-[80%] mx-auto mt-4">
        {localStorage.getItem("role") === "agent" && (
          <div className="my-6">
            <span className="font-bold text-xl">Sold</span>
            <div className="grid xl:grid-cols-4 md:grid-cols-2 gap-10 mt-4">
              {data?.sold.map((card_data) => (
                <TransCard info={card_data} key={card_data.transaction_id} />
              ))}
            </div>
          </div>
        )}
        <div>
          <span className="font-bold text-xl">Bought</span>
          <div className="grid xl:grid-cols-4 md:grid-cols-2 gap-10 mt-4">
            {data?.bought.map((card_data) => (
              <TransCard info={card_data} key={card_data.transaction_id} />
            ))}
          </div>
        </div>
      </div>
    </>
  );
};

export default Trans;
