import { useNavigate } from "react-router-dom";

/* eslint-disable react/prop-types */
const Card = ({ info }) => {
  const navigate = useNavigate();
  return (
    <div
      className="rounded overflow-hidden border border-black p-2 shadow-xl hover:cursor-pointer hover:scale-110 transform transition duration-75"
      onMouseUp={() => navigate(`/listing/${info.PROPERTY_ID}`)}
    >
      <div className="flex flex-col mb-4">
        <span className="font-bold text-2xl">{info.TITLE}</span>
        <span className="text-gray-600 text-sm mb-2">By {info.USER_NAME}</span>
        <hr />
        <span className="text-xl">₹{info.PRICE}</span>
        <span className="text-sm">{info.CITY}</span>
        <span className="text-sm">{info.STATE}</span>
        <span>{info.AVAILABILITY_STATUS}</span>
        <span className="text-md text-gray-600">{info.PROPERTY_TYPE}</span>
      </div>
      <div className="flex flex-col mb-2">
        <table className=" rounded-md">
          <tbody>
            <tr>
              <td className="border border-black">Sqarue foot</td>
              <td className="border border-black">{info.SIZE_OF_PROPERTY}</td>
            </tr>
            <tr>
              <td className="border border-black">BHK</td>
              <td className="border border-black">{info.BHK}</td>
            </tr>
            <tr>
              <td className="border border-black">Bedrooms</td>
              <td className="border border-black">{info.BEDROOMS}</td>
            </tr>
            <tr>
              <td className="border border-black">Kitchens</td>
              <td className="border border-black">{info.KITCHEN}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <hr
        className={`absolute bottom-0 border-4 ${info.AVAILABILITY_STATUS === "Sold" ? "border-red-500" : ""} ${info.AVAILABILITY_STATUS === "Available" ? "border-green-500" : ""} w-full left-0`}
      />
    </div>
  );
};

export default Card;
