import React from 'react';
import ItemData from '../models/ItemData';
import styles from './ItemComponent.module.css'; // Importa o módulo de estilo CSS
import camisaImage from "./camisa.jpg";

interface ItemProps {
  item: ItemData;
}

const ItemComponent: React.FC<ItemProps> = ({ item }) => {
    
  return (
    <div className={styles.itemCard}>
        <div className={styles.itemImage}>
            <img src={camisaImage} alt={item.nome}/>
        </div>
    <div className={styles.itemInfo}>
        <h2 className={styles.itemName}>{item.nome}</h2>
        <p className={styles.itemDescription}>{item.description}</p>
        <div className={styles.itemPriceQuantity}>
          <p className={styles.itemPrice}>{item.price}</p>
          <div className={styles.itemQuantity}>
            <button className={styles.quantityMinus}>-</button>
            <span className={styles.quantityPlus}>{item.quantidade}</span>
            <button className={styles.quantityValue}>+</button>
          </div>
        </div>
        <button className={styles.itemRemove}>Remover</button>
    </div>
    </div>
  );
};

export default ItemComponent;