import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import { useState } from "react";
import { useParams } from "react-router-dom";
import { useEffect } from "react";

const EditListing = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [data, setData] = useState([]);
  useEffect(() => {
    const getData = async () => {
      const url = `https://apex.oracle.com/pls/apex/tushya/proj/editlisting/${id}?token_=${localStorage.getItem("token")}`;
      const res = await fetch(url, {
        method: "GET",
      });
      const obj = await res.json();
      if (obj.status === 401) {
        navigate("/logout");
      } else if (obj.status === 403) {
        alert("You can only edit your own listings");
        navigate("/");
      }
      setData(obj.data[0]);
    };
    getData();
  }, [id, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const title = e.target[0].value;
    const state = e.target[1].value;
    const city = e.target[2].value;
    const address = e.target[3].value;
    const property_type = e.target[4].value;
    const size_of_property = e.target[5].value;
    const bhk = e.target[6].value;
    const kitchen = e.target[7].value;
    const bedrooms = e.target[8].value;
    const price = e.target[9].value;
    const availability_status = e.target[10].value;
    const url = `https://apex.oracle.com/pls/apex/tushya/proj/editlisting/${id}`;
    const res = await fetch(url, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token_: localStorage.getItem("token"),
        title_: title,
        property_id_: data.PROPERTY_ID,
        address_: address,
        city_: city,
        state_: state,
        property_type_: property_type,
        price_: price,
        size_of_property_: size_of_property,
        bhk_: bhk,
        bedrooms_: bedrooms,
        kitchen_: kitchen,
        availability_status_: availability_status,
      }),
    });
    const obj = await res.json();
    if (obj.status === 203) {
      navigate(`/listing/${id}`);
    } else if (obj.status === 409) {
      e.target[1].value = "";
      e.target[2].value = "";
      alert("User already exists");
    } else if (obj.status === 500) {
      alert("Server error please try again");
    } else if (obj.status === 401) {
      navigate("/logout");
    }
  };

  return (
    <>
      <Navbar />
      <div className="w-full h-screen flex items-center justify-center">
        <div className="border border-black shadow-xl rounded-md w-96 py-4 mt-16">
          <h1 className="text-center mx-auto font-bold text-2xl mb-8">
            {"Edit Listing"}
          </h1>
          <form className="flex flex-col gap-2 px-4" onSubmit={handleSubmit}>
            <label htmlFor="title">Title</label>
            <input
              type="text"
              name="title"
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
              defaultValue={data.TITLE}
              required
            />
            <label htmlFor="state">State</label>
            <input
              type="text"
              name="state"
              defaultValue={data.STATE}
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
              required
            />
            <label htmlFor="city">City</label>
            <input
              type="text"
              name="city"
              defaultValue={data.CITY}
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
              required
            />
            <label htmlFor="address">Address</label>
            <input
              type="text"
              name="Address"
              defaultValue={data.ADDRESS}
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
              required
            />
            <label htmlFor="type">Type</label>
            <select
              name="type"
              id="type"
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
            >
              <option value="Apartment">Apartment</option>
              <option value="Villa">Villa</option>
              <option value="Flat">Flat</option>
            </select>
            <label htmlFor="size">Size</label>
            <input
              type="number"
              name="size"
              defaultValue={data.SIZE_OF_PROPERTY}
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
              required
            />
            <label htmlFor="bhk">BHK</label>
            <input
              type="number"
              name="bhk"
              defaultValue={data.BHK}
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
              required
            />
            <label htmlFor="kitchen">Kitchen</label>
            <input
              type="number"
              name="kitchen"
              defaultValue={data.KITCHEN}
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
              required
            />
            <label htmlFor="bedroom">Bedroom</label>
            <input
              type="number"
              name="bedroom"
              defaultValue={data.BEDROOMS}
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
              required
            />
            <label htmlFor="price">Price</label>
            <input
              type="number"
              name="price"
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
              defaultValue={data.PRICE}
              required
            />
            <label htmlFor="availability">Availability</label>
            <select
              name="availability"
              id="availablility"
              className="border-b-2 border-gray-400 bg-white pl-2 h-8"
            >
              <option value="Available">Available</option>
              <option value="Sold">Sold</option>
              <option value="Under Contract">Under Contract</option>
            </select>
            <input
              type="submit"
              value="Submit"
              className="border border-black rounded-full w-32 px-4 py-2 mx-auto bg-green-300 mt-8 hover:cursor-pointer"
            />
          </form>
        </div>
      </div>
    </>
  );
};

export default EditListing;
