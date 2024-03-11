import GetCart from "../../components/getCart";
import GoToItemPageButton from "../../components/GoToItemPageButton";
import './index.css';

const ViewCart = () => {
    return (
        <div className="cartContainer">
            <div className="goToItemPageContainer">
                <GoToItemPageButton />
            </div>
            <div className="getCartContainer">
                <GetCart />
            </div>
        </div>
    );
};

export default ViewCart;
