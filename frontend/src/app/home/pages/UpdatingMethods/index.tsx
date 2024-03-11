import styles from "./index.module.css";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import Button from "../../components/buttom";
import ReturnButton from "../../components/ReturnButton";
import { useNavigate } from 'react-router-dom';
import {useState} from 'react'
import axios from "axios";
import SubmitButton from "../../components/SubmitButton";

const UpdatingMethod = () => {

    const navigate = useNavigate(); 

    const handleBoletoClick = () => {

        navigate("/paymentMethod/updating/boleto")

    }

    const handleCartaoClick = ()  => {

        navigate("/paymentMethod/updating/cartao")

    }

    const handlePixClick = ()  => {

        navigate("/paymentMethod/updating/pix")

    }

    return (
        <div >
            <Pichu></Pichu>
            <Message value="Selecione uma forma de pagamento para atualizar"></Message>
            <div className={styles.container}>
                <Button value = "Boleto" DataCy="select_update_boleto"onClick={handleBoletoClick}></Button>
                <Button value = "Cartão de débito"  DataCy="select_update_cartao" onClick={handleCartaoClick}></Button>
            </div>
            <div className={styles.container}>
                <Button value="Pix"  DataCy="select_update_pix" onClick={handlePixClick}></Button>
            </div>
            <ReturnButton path = "/paymentMethod"></ReturnButton>
        </div>
        

    )

}


export default UpdatingMethod; 