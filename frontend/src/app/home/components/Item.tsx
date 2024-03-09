import React from 'react';
import ItemData from '../models/ItemData';
import styles from './ItemComponent.module.css';
import camisaImage from "./camisa.jpg";
import RemoveFromCartButton from './RemoveFromCartButton';
import IncreaseItemQuantityButton from './IncreaseItemQuantity';
import { useCpf } from '../context/HomeContext/CpfContext';

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

  const handleError = (message: string) => {
    console.error(message);
  };

  const decreaseQuantity = () => {
    // Implementar lógica para diminuir a quantidade do item
    onItemChange(); // Notifica o componente pai sobre a mudança
  };

  return (
    <div className={styles.itemCard}>
      <div className={styles.itemImage}>
        <img src={camisaImage} alt={item.nome} />
      </div>
      <div className={styles.itemInfo}>
        <h2 className={styles.itemName}>{item.nome}</h2>
        <p className={styles.itemDescription}>{item.description}</p>
        <div className={styles.itemPriceQuantity}>
          <p className={styles.itemPrice}>{item.price}</p>
          <div className={styles.itemQuantity}>
            <button className={styles.quantityMinus} onClick={decreaseQuantity}>-</button>
            <span className={styles.quantityValue}>{item.quantidade}</span>
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
