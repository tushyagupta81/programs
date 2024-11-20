import { useParams } from "react-router-dom";
import Navbar from "../components/Navbar";
import { useEffect } from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Listing = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [data, setData] = useState([]);

  const handleDelete = async () => {
    const url = `https://apex.oracle.com/pls/apex/tushya/proj/delete/${id}?token_=${localStorage.getItem("token")}`;
    const res = await fetch(url, {
      method: "DELETE",
    });
    const obj = await res.json();
    if (obj.status === 200) {
      navigate("/");
    } else if (obj.status === 401) {
      navigate("/logout");
    } else if (obj.status === 409) {
      alert("Cannot delete property under sale");
    } else if (obj.status === 403) {
      alert("You can only delete your own listing");
    }
  };

  const handleBuy = async () => {
    const url = `https://apex.oracle.com/pls/apex/tushya/proj/buy/${id}`;
    const res = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token_: localStorage.getItem("token"),
        payment_method_: "Cash",
      }),
    });
    const obj = await res.json();
    if (obj.status === 201) {
      navigate("/");
    } else if (obj.status === 401) {
      navigate("/logout");
    } else if (obj.status === 403) {
      alert("Cannot buy your own property");
    }
  };

  useEffect(() => {
    const getData = async () => {
      const url = `https://apex.oracle.com/pls/apex/tushya/proj/getproperty/${id}?token_=${localStorage.getItem("token")}`;
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
  }, [id, navigate]);

  return (
    <>
      <Navbar />
      <div className="flex flex-col w-[80%] mt-8 mx-auto">
        <div className="flex flex-row justify-between items-center">
          <span className="text-3xl font-bold">{data.TITLE}</span>
          <span
            className={`px-2 border border-black ${data.AVAILABILITY_STATUS === "Available" ? "bg-green-300" : "bg-gray-300"} rounded-full`}
          >
            {data.AVAILABILITY_STATUS}
          </span>
        </div>
        <hr className="mb-4" />
        <div className="flex flex-row justify-between items-center">
          <span className="text-xl font-bold">₹{data.PRICE}</span>
          <span className="text-xl text-gray-500">{data.PROPERTY_TYPE}</span>
        </div>
        <div className="mt-4">
          <div className="flex flex-row gap-4">
            <span>City</span>
            <span>{data.CITY}</span>
          </div>
          <div className="flex flex-row gap-4">
            <span>State</span>
            <span>{data.STATE}</span>
          </div>
          <div className="flex flex-row gap-4">
            <span>Address</span>
            <span>{data.ADDRESS}</span>
          </div>
        </div>
        <table className="mt-4 w-64">
          <tbody>
            <tr>
              <td className="border border-black">Sqarue foot</td>
              <td className="border border-black">{data.SIZE_OF_PROPERTY}</td>
            </tr>
            <tr>
              <td className="border border-black">BHK</td>
              <td className="border border-black">{data.BHK}</td>
            </tr>
            <tr>
              <td className="border border-black">Bedrooms</td>
              <td className="border border-black">{data.BEDROOMS}</td>
            </tr>
            <tr>
              <td className="border border-black">Kitchens</td>
              <td className="border border-black">{data.KITCHEN}</td>
            </tr>
          </tbody>
        </table>
        <table className="w-64 mt-4">
          <tbody>
            <tr>
              <td className="font-bold">Seller</td>
              <td className="text-md">{data.USER_NAME}</td>
            </tr>
            <tr>
              <td className="font-bold">Seller email</td>
              <td className="text-md">{data.USER_EMAIL}</td>
            </tr>
            <tr>
              <td className="font-bold">Seller phone</td>
              <td className="text-md">{data.USER_PHONE}</td>
            </tr>
          </tbody>
        </table>

        <div className="flex flex-row pt-4 gap-4">
          {Number.parseInt(localStorage.getItem("id")) ===
          Number.parseInt(data.USER_ID) ? (
            <>
              <button
                type="button"
                className="border border-blue-500 bg-blue-300 rounded-xl py-1 px-2"
                onMouseUp={() => navigate(`/editlisting/${id}`)}
              >
                Edit
              </button>
              {data.AVAILABILITY_STATUS === "Available" && (
                <button
                  type="button"
                  className="border border-red-500 bg-red-300 rounded-xl py-1 px-2"
                  onMouseUp={handleDelete}
                >
                  Delete
                </button>
              )}
            </>
          ) : (
            <></>
          )}
          {data.AVAILABILITY_STATUS === "Available" &&
          !(
            Number.parseInt(localStorage.getItem("id")) ===
            Number.parseInt(data.USER_ID)
          ) ? (
            <button
              type="button"
              className="border border-green-500 bg-green-300 rounded-xl py-1 px-2"
              onMouseUp={handleBuy}
            >
              Buy
            </button>
          ) : (
            <></>
          )}
        </div>
      </div>
    </>
  );
};

export default Listing;
