import React from 'react';
import ItemData from '../models/ItemData';
import styles from './ItemComponent.module.css'; // Importa o módulo de estilo CSS

interface ItemProps {
  item: ItemData;
}

const ItemComponent: React.FC<ItemProps> = ({ item }) => {
  return (
    <div className={styles.itemContainer}>
      <div>ID: {item.id}</div>
      <div>Nome: {item.nome}</div>
      <div className={styles.itemInfo}>
        <div className={styles.price}>Preço: {item.price}</div>
        <div className={styles.quantity}>Quantidade: {item.quantidade}</div>
      </div>
      {item.img && <img src={item.img} alt="Imagem do item" />}
    </div>
  );
};

export default ItemComponent;