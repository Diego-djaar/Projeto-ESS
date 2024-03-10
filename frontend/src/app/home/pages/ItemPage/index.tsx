import AddToCartButton from "../../components/AddToCartButton";
import ItemData from "../../models/ItemData";
import { useCpf } from "../../context/HomeContext/CpfContext";

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
        <AddToCartButton
        item = {itemExemplo}
        cpf = {cpf}
        onItemAdded={handleItemAdded}
        onError={handleError}
        />
    </>)
};

export default ItemPage