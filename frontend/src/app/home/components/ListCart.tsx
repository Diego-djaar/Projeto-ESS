import ItemData from "../models/ItemData";
import ItemComponent from "./Item";
import styles from "./ListCart.module.css";

function ListCart() {
    const item: ItemData = {
        id: '12345678',
        nome: 'Item de Exemplo',
        description: 'Descrição do item de exemplo',
        price: '$10.00',
        quantidade: 5,
        img: './camisa.jpg'
      };

    return (
        <div className='aaa'>
          <ItemComponent item={item} />
        </div>
    );
};

export default ListCart