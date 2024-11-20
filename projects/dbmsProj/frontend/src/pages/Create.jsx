import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";

const Create = () => {
  const navigate = useNavigate();
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
    const res = await fetch(
      "https://apex.oracle.com/pls/apex/tushya/proj/create/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token_: localStorage.getItem("token"),
          title_: title,
          address_: address,
          city_: city,
          state_: state,
          property_type_: property_type,
          price_: price,
          size_of_property_: size_of_property,
          bhk_: bhk,
          bedrooms_: bedrooms,
          kitchen_: kitchen,
        }),
      },
    );
    const obj = await res.json();
    if (obj.status === 201) {
      navigate("/");
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
        <div className="border border-black shadow-xl rounded-md w-96 py-4">
          <h1 className="w-min mx-auto font-bold text-2xl">Create Listing</h1>
          <form className="flex flex-col gap-2 px-4" onSubmit={handleSubmit}>
            <label htmlFor="title">Title</label>
            <input
              type="text"
              name="title"
              className="border border-black rounded-md h-8 pl-2"
              required
            />
            <label htmlFor="state">State</label>
            <input
              type="text"
              name="state"
              className="border border-black rounded-md h-8 pl-2"
              required
            />
            <label htmlFor="city">City</label>
            <input
              type="text"
              name="city"
              className="border border-black rounded-md h-8 pl-2"
              required
            />
            <label htmlFor="address">Address</label>
            <input
              type="text"
              name="Address"
              className="border border-black rounded-md h-8 pl-2"
              required
            />
            <label htmlFor="type">Type</label>
            <select
              name="type"
              id="type"
              className="border blorder-black h-8 rounded-md pl-2"
            >
              <option value="Apartment">Apartment</option>
              <option value="Villa">Villa</option>
              <option value="Flat">Flat</option>
            </select>
            <label htmlFor="size">Size</label>
            <input
              type="number"
              name="size"
              className="border border-black rounded-md h-8 px-2"
              required
            />
            <label htmlFor="bhk">BHK</label>
            <input
              type="number"
              name="bhk"
              className="border border-black rounded-md h-8 px-2"
              required
            />
            <label htmlFor="kitchen">Kitchen</label>
            <input
              type="number"
              name="kitchen"
              className="border border-black rounded-md h-8 px-2"
              required
            />
            <label htmlFor="bedroom">Bedroom</label>
            <input
              type="number"
              name="bedroom"
              className="border border-black rounded-md h-8 px-2"
              required
            />
            <label htmlFor="price">Price</label>
            <input
              type="number"
              className="border border-black rounded-md h-8 px-2"
              required
            />
            <input
              type="submit"
              value="Submit"
              className="border border-black rounded-full w-min px-4 py-2 mx-auto bg-green-300 mt-2"
            />
          </form>
        </div>
      </div>
    </>
  );
};

export default Create;
