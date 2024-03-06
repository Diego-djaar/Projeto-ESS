import styles from "./index.module.css";
import Button from "../../components/buttom";
import { useNavigate } from 'react-router-dom';

const PaymentConfig = () => {

    const navigate = useNavigate()

    const handleInsertingClick = () => {

        navigate("/paymentMethod/inserting")
    }

    return (
        <div className={styles.background}>
            <div>
                <img src="../../../../../public/Pichu.png" alt="" className={styles.image}/>
            </div>
            <p className={styles.mensage}>Configurações de método de pagamento</p>
            <div className = {styles.buttomContainer}>
                <div>
                    <div onClick={handleInsertingClick}>
                        <Button value="Inserir método de pagamento" ></Button>
                    </div>
                    <Button value="Atualizar método de pagamento"></Button>
                </div>
                <div>
                    <Button value="Deletar método de pagamento" ></Button>
                    <Button value="Visualizar método de pagamento" ></Button>
                </div>
            </div>
        </div>
    )
}

export default PaymentConfig;
