import AddToCartButton from "../../components/AddToCartButton";
import ItemData from "../../models/ItemData";
import { useCpf } from "../../context/HomeContext/CpfContext";
import GoToCartButton from "../../components/GoToCartButton";
import styles from './index.module.css'

const ItemPage = () => {
    const [ cpf ] = useCpf();
    const itemExemplo: ItemData = {
        id: "12345678", // Um ID de exemplo
        nome: "Camiseta Azul", // Nome do item
        description: "Uma camiseta azul de algodão com gola redonda", // Descrição do item
        price: "29.90", // Preço do item
        quantidade: 1, // Quantidade em estoque ou quantidade desejada pelo usuário
        img: "imagem.jpg", // Pode ser null se não houver imagem
      };

    const handleItemAdded = () => {
        console.log('Item adicionado com sucesso');
    };

    const handleError = (message: string) => {
        console.error(message);
    };

    return (<>
        <div className={styles.itemPage}>
            <div className={styles.itemDetails}>
                <h1>{itemExemplo.nome}</h1>
                <p>{itemExemplo.description}</p>
                <p>Preço: R${itemExemplo.price}</p>
                <AddToCartButton
                    item={itemExemplo}
                    cpf={cpf}
                    onItemAdded={handleItemAdded}
                    onError={handleError}
                />
            </div>
            <div className={styles.goToCartButton}>
                <GoToCartButton itemCount={1} />
            </div>
        </div>
    </>)
};

export default ItemPage