import { useNavigate } from "react-router-dom";

/* eslint-disable react/prop-types */
const TransCard = ({ info }) => {
  const navigate = useNavigate();
  return (
    <div
      className="rounded overflow-hidden border border-black p-2 shadow-xl hover:cursor-pointer hover:scale-110 transform transition duration-75 relative"
      onMouseDown={() => navigate(`/transaction/${info.TRANSACTION_ID}`)}
    >
      <div className="flex flex-col mb-4">
        <span className="font-bold text-2xl">
          Transaction id: {info.TRANSACTION_ID}
        </span>
        <hr />
        <span className="text-gray-600 text-sm mt-1">
          From {info.BUYER_NAME} to {info.SELLER_NAME}
        </span>
        <span className="text-xl">₹{info.TRANSACTION_AMOUNT}</span>
        <span>
          {info.TRANSACTION_DATE.split("T").map(
            (word) => `${word.split("Z")[0]} `,
          )}
        </span>
        <span>{info.PAYMENT_METHOD}</span>
        <span>{info.PAYMENT_STATUS}</span>
      </div>
      <hr
        className={`absolute bottom-0 border-4 ${info.PAYMENT_STATUS === "Completed" ? "border-green-500" : "border-red-500"} w-full left-0`}
      />
    </div>
  );
};

export default TransCard;
