import { useParams } from "react-router-dom";
import Navbar from "../components/Navbar";
import { useEffect } from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Listing = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [data, setData] = useState([]);
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
          <span className="px-2 border border-black bg-green-300 rounded-full">
            {data.AVAILABILITY_STATUS}
          </span>
        </div>
        <hr className="mb-4" />
        <div className="flex flex-row justify-between items-center">
          <span className="text-xl font-bold">₹{data.PRICE}</span>
          <span className="text-xl text-gray-500">{data.PROPERTY_TYPE}</span>
        </div>
        <span>City: {data.CITY}</span>
        <span>State: {data.STATE}</span>
        <span>Address: {data.ADDRESS}</span>
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
      </div>
    </>
  );
};

export default Listing;
