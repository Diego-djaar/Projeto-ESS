import React from 'react';
import ItemData from '../models/ItemData';
import './ItemComponent.css';
import camisaImage from "./camisa.jpg";
import RemoveFromCartButton from './RemoveFromCartButton';
import IncreaseItemQuantityButton from './IncreaseItemQuantity';
import { useCpf } from '../context/HomeContext/CpfContext';
import DecreaseItemQuantityButton from './DecreaseItemQuantity';

interface ItemProps {
  item: ItemData;
  onItemChange: () => void; // Prop para notificar mudanças no item
}

const ItemComponent: React.FC<ItemProps> = ({ item, onItemChange }) => {
  const [cpf] = useCpf(); // Assumindo que useCpf retorna um objeto com cpf

  const handleItemRemoved = () => {
    console.log("Item removido com sucesso");
    onItemChange(); // Notifica o componente pai que um item foi removido
  };

  const handleIncrease = () => {
    console.log("Item incrementado com sucesso");
    onItemChange();
  }

  const handleDecrease = () => {
    console.log("Item decrementado com sucesso");
    onItemChange();
  }

  const handleError = (message: string) => {
    console.error(message);
  };

  return (
    <div className="itemCard">
      <div className="itemImage">
        <img src={camisaImage} alt={item.nome} />
      </div>
      <div className="itemInfo">
        <h2 className="itemName">{item.nome} <span className="itemID">(ID: {item.id})</span> </h2>
        <p className="itemDescription">{item.description}</p>
        <div className="itemPriceQuantity">
          <p className="itemPrice">{item.price}</p>
          <div className="itemQuantity">
            <DecreaseItemQuantityButton 
            itemId={item.id}
            cpf={cpf}
            onItemDecreaseQuantity={handleDecrease}
            onError={handleError}
            />
            <span className="quantityValue">{item.quantidade}</span>
            <IncreaseItemQuantityButton
            itemId={item.id}
            cpf={cpf}
            onItemIncreaseQuantity={handleIncrease}
            onError={handleError}
            />
          </div>
        </div>
        <RemoveFromCartButton 
          itemId={item.id}
          cpf={cpf}
          onItemRemoved={handleItemRemoved}
          onError={handleError}
        />
      </div>
    </div>
  );
};

export default ItemComponent;
