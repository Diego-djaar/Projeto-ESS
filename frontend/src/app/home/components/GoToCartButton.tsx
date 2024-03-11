import React from 'react';
import { Link } from 'react-router-dom';
import cartIcon from '../assets/cartIcon.jpg'
import './GoToCartButton.css'

interface CartButtonProps {
  itemCount: number; // A quantidade de itens no carrinho
}

const CartButton: React.FC<CartButtonProps> = ({ itemCount }) => {
  return (
    <Link to="/carrinho" className="cartButton">
      <img src={cartIcon} alt="Carrinho" />
      {itemCount > 0 && <span className="itemCount">{itemCount}</span>}
    </Link>
  );
};

export default CartButton;
