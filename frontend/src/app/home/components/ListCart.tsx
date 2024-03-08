import ItemData from "../models/ItemData";
import ItemComponent from "./Item";
import styles from "./ListCart.module.css"

function ListCart() {
    const item: ItemData = {
        id: '12345678',
        nome: 'Item de Exemplo',
        description: 'Descrição do item de exemplo',
        price: '$10.00',
        quantidade: 5,
        img: 'caminho/para/imagem.jpg'
      };

    return (
        <div className={styles.list}>
          <ItemComponent item={item} />
        </div>
    );
};

export default ListCart