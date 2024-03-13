import styles from "./index.module.css";
import Button from "../../components/buttom";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import ReturnButton from "../../components/ReturnButton";
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
                <Button DataCy = "select_boleto" value = "Boleto" onClick={handleBoletoClick}></Button>
                <Button  DataCy = "select_cartao" value = "Cartão de débito" onClick={handleCartaoClick}></Button>
            </div>
            <div className={styles.container}>
                <Button  DataCy = "select_pix" value="Pix" onClick={handlePixClick}></Button>
            </div>
            <ReturnButton path="/paymentMethod"></ReturnButton>
        </div>
        

    )

}

export default PaymentInserting;