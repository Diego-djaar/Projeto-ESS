import styles from "./index.module.css";
import Button from "../../components/buttom";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import { useNavigate } from 'react-router-dom';


const PaymentInserting = () => {

    const navigate = useNavigate()

    const handleBoletoClick = () => {

        navigate("/paymentMethod/inserting/boleto")
    }

    const handleCartaoClick = () => {

        navigate("/paymentMethod/inserting/cartao")
    }

    const handlePixClick = () => {

        navigate("/paymentMethod/inserting/pix")
    }

    return (
        <div >
            <Pichu></Pichu>
            <Message value="Selecione uma forma de pagamento"></Message>
            <div className={styles.container}>
                <Button value = "Boleto" onClick={handleBoletoClick}></Button>
                <Button value = "Cartão de débito" onClick={handleCartaoClick}></Button>
            </div>
            <div className={styles.container}>
                <Button value="Pix" onClick={handlePixClick}></Button>
            </div>
        </div>
        

    )

}

export default PaymentInserting;