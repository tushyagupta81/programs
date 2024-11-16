import Card from "../components/Card";
import Navbar from "../components/Navbar";

const Home = () => {
  return (
    <>
      <Navbar />
      <div>Home</div>
      <h1>Home</h1>
      <div className="grid xl:grid-cols-4 md:grid-cols-2 gap-10 w-[80%] mx-auto">
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
      </div>
    </>
  );
};

export default Home;
