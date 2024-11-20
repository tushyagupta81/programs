import { useEffect } from "react";
import { useState } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";

const OneTrans = () => {
  const navigate = useNavigate();
  const { id } = useParams();
  const [data, setData] = useState({});

  const handleComplete = async () => {
    const url = `https://apex.oracle.com/pls/apex/tushya/proj/completetrans/${id}`;
    const res = await fetch(url, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token_: localStorage.getItem("token"),
      }),
    });
    const obj = await res.json();
    if (obj.status === 203) {
      navigate("/transactions");
    } else if (obj.status === 500) {
      alert("Server error please try again");
    } else if (obj.status === 401) {
      navigate("/logout");
    } else if (obj.status === 403) {
      alert("Cannot change this transaction");
    }
  };

  useEffect(() => {
    const getData = async () => {
      const url = `https://apex.oracle.com/pls/apex/tushya/proj/gettransaction/${id}?token_=${localStorage.getItem("token")}`;
      const res = await fetch(url, {
        method: "GET",
      });
      const obj = await res.json();
      if (obj.status === 401) {
        navigate("/logout");
      }
      setData(obj.data[0]);
    };
    getData();
  }, [navigate, id]);
  return (
    <>
      <Navbar />
      <div className="flex flex-col mb-4 w-[80%] mx-auto mt-8">
        <span className="font-bold text-2xl">
          Transaction id: {data.TRANSACTION_ID}
        </span>
        <span className="text-gray-600 text-sm">
          From {data.BUYER_NAME} to {data.SELLER_NAME}
        </span>
        <hr className="py-2" />
        <span className="text-xl">₹{data.TRANSACTION_AMOUNT}</span>
        <span>
          {data.TRANSACTION_DATE?.split("T").map(
            (word) => `${word.split("Z")[0]} `,
          )}
        </span>
        <span>{data.PAYMENT_METHOD}</span>
        <span> {data.PAYMENT_STATUS}</span>
        <div>
          {Number.parseInt(localStorage.getItem("id")) ===
            Number.parseInt(data.SELLER_ID) &&
          data.PAYMENT_STATUS !== "Completed" ? (
            <button
              type="button"
              className="border border-blue-500 bg-blue-300 rounded-xl py-1 px-2"
              onMouseUp={handleComplete}
            >
              Mark as Done
            </button>
          ) : (
            <></>
          )}
        </div>
      </div>
    </>
  );
};

export default OneTrans;
