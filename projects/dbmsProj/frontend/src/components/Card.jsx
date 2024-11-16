const Card = () => {
  return (
    <div className="rounded overflow-hidden border border-black p-2 shadow-xl">
      <div className="flex flex-col mb-4">
        <span className="font-bold text-2xl">Title</span>
        <span className="text-gray-600 text-sm">By xyz</span>
        <span className="text-xl">Price</span>
      </div>
      <div className="flex flex-col">
        <table className=" rounded-md">
          <tr>
            <td className="border border-black">Sqarue foot</td>
            <td className="border border-black">1000</td>
          </tr>
          <tr>
            <td className="border border-black">BHK</td>
            <td className="border border-black">3</td>
          </tr>
          <tr>
            <td className="border border-black">Bedrooms</td>
            <td className="border border-black">3</td>
          </tr>
          <tr>
            <td className="border border-black">Kitchens</td>
            <td className="border border-black">1</td>
          </tr>
        </table>
      </div>
    </div>
  );
};

export default Card;
