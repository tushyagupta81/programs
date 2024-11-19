import { useNavigate } from "react-router-dom";

/* eslint-disable react/prop-types */
const TransCard = ({ info }) => {
  const navigate = useNavigate();
  return (
    <div
      className="rounded overflow-hidden border border-black p-2 shadow-xl"
      onMouseDown={() => navigate(`/transaction/${info.TRANSACTION_ID}`)}
    >
      <div className="flex flex-col mb-4">
        <span className="font-bold text-2xl">
          Transaction id: {info.TRANSACTION_ID}
        </span>
        <span className="text-gray-600 text-sm">
          From {info.BUYER_ID} to {info.SELLER_ID}
        </span>
        <span className="text-xl">₹{info.TRANSACTION_AMOUNT}</span>
        <span>
          {info.TRANSACTION_DATE.split("T").map(
            (word) => `${word.split("Z")} `,
          )}
        </span>
        <span>{info.PAYMENT_METHOD}</span>
        <span> {info.PAYMENT_STATUS}</span>
      </div>
    </div>
  );
};

export default TransCard;
