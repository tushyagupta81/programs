import { useNavigate } from "react-router-dom";

/* eslint-disable react/prop-types */
const Card = ({ info }) => {
  const navigate = useNavigate();
  console.log(info);
  return (
    <div
      className="rounded overflow-hidden border border-black p-2 shadow-xl"
      onMouseUp={() => navigate(`/listing/${info.PROPERTY_ID}`)}
    >
      <div className="flex flex-col mb-4">
        <span className="font-bold text-2xl">{info.TITLE}</span>
        <span className="text-gray-600 text-sm">By {info.USER_NAME}</span>
        <span className="text-xl">{info.PRICE}</span>
      </div>
      <div className="flex flex-col">
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
    </div>
  );
};

export default Card;
