const Button = ({
  label,
  iconURL,
  backgroundColor,
  borderColor,
  textColor,
  fullwidth,
}) => {
  return (
    <button
      className={`flex justify-center items-center gap-2 px-7 py-4 border font-montserrat text-lg leading-none 
      ${backgroundColor ? backgroundColor : "bg-coral-red"} rounded-full ${textColor ? textColor : "text-white"} 
      ${borderColor ? borderColor : "border-coral-red"} ${fullwidth && "w-full"}`}
    >
      {label}
      {iconURL && (
        <img src={iconURL} alt="icon" className="ml-2 rounded-full w-5 h-5" />
      )}
    </button>
  );
};

export default Button;
