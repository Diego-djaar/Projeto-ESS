import styles from "./index.module.css";
import Button from "../../components/buttom";
import Pichu from "../../components/logo";
import Mensage from "../../components/mensage";
import { useNavigate } from 'react-router-dom';

const PaymentConfig = () => {

    const navigate = useNavigate()

    const handleInsertingClick = () => {

        navigate("/paymentMethod/inserting")
    }

    const handleUpdatingClick = () => {

        navigate("/paymentMethod/updating")
    }

    const handleDeletingClick = () => {

        navigate("/paymentMethod/inserting")
    }

    const handleViewingClick = () => {

        navigate("/paymentMethod/inserting")
    }

    return (
        <div className={styles.background}>
            <div>
                <Pichu></Pichu>
            </div>
            <Mensage value= "Configurações de método de pagamento"></Mensage>
            <div className = {styles.buttomContainer}>
                <div>
                    <Button value="Inserir método de pagamento" onClick={handleInsertingClick}></Button>
                    <Button value="Atualizar método de pagamento" onClick={handleUpdatingClick}></Button>
                </div>
                <div>
                    <Button value="Deletar método de pagamento" onClick={handleDeletingClick}></Button>
                    <Button value="Visualizar método de pagamento" onClick={handleViewingClick}></Button>
                </div>
            </div>
        </div>
    )
}

export default PaymentConfig;
