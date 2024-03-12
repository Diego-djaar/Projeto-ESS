import GetCart from "../../Components/Carrinho/getCart";
import GoToItemPageButton from "../../Components/Carrinho/GoToItemPageButton";
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
