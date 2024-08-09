import { reviews } from "../constants";
import { ReviewCard } from "../components";

const CustomerReviews = () => {
  return (
    <section className="max-conatiner">
      <h3 className="font-palanquin text-center text-4xl font-bold">
        What our <span className="text-coral-red">Customers</span> Say?
      </h3>
      <p className="info-text m-auto mt-4 max-x-lg text-center">
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Inventore
        ipsam consequatur beatae dolorem, quod deserunt alias accusantium
        expedita veniam exercitationem incidunt eligendi sit. Iusto, eaque velit
        impedit soluta quaerat incidunt.
      </p>
      <div className="mt-24 flex flex-1 justify-evenly items-center max-lg:flex-col gap-14">
        {reviews.map((review) => (
          <ReviewCard
            key={review.customerName}
            imgURL={review.imgURL}
            customerName={review.customerName}
            rating={review.rating}
            feedback={review.feedback}
          />
        ))}
      </div>
    </section>
  );
};

export default CustomerReviews;
