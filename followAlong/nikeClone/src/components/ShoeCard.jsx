const ShoeCard = ({ imageURL, changeBigShoeImage, bigShoeImage }) => {
  function handleClick() {
    if (bigShoeImage !== imageURL.bigShoe) {
      changeBigShoeImage(imageURL.bigShoe);
    }
  }
  return (
    <div
      className={`border-2 rounded-xl ${bigShoeImage === imageURL.bigShoe ? "border-coral-red" : "border-transparent"} cursor-pointer max-sm:flex-1`}
      onClick={handleClick}
    >
      <div className="flex justify-center items-center bg-card bg-center bg-cover sm:w-40 sm:h-40 rounded-xl max-sm:p-4">
        <img
          src={imageURL.bigShoe}
          alt="shoe coll"
          width={120}
          height={103}
          className="object-contain"
        />
      </div>
    </div>
  );
};

export default ShoeCard;
