import { Button } from "../components";
import { arrowRight } from "../assets/icons";
import { offer } from "../assets/images";

const SpecialOffer = () => {
  return (
    <section className="flex justify-wrap items-center max-xl:flex-col-reverse col-10 max-container">
      <div className="flex-1 sm:mt-10">
        <img
          src={offer}
          width={773}
          height={687}
          className="w-full object-contain"
          alt="offer"
        />
      </div>
      <div className="flex flex-1 flex-col">
        <h2 className="font-palanquin text-4xl capitalize font-bold lg:max-w-lg">
          <span className="text-coral-red">Special </span>Offers
        </h2>
        <p className="mt-4 info-text">
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quia eveniet
          exercitationem eius vel maiores mollitia cumque, asperiores voluptate
          alias aut, quam atque culpa commodi temporibus repudiandae tempore
          veritatis rerum neque!
        </p>
        <p className="mt-6 info-text">
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quia eveniet
          exercitationem eius vel maiores mollitia
        </p>
        <div className="mt-11 flex flex-wrap gap-4">
          <Button label="Show now" iconURL={arrowRight} />
          <Button
            label="Learn More"
            backgroundColor="bg-white"
            border-color="border-slate-grey"
            textColor="text-slate-gray"
          />
        </div>
      </div>
    </section>
  );
};

export default SpecialOffer;
