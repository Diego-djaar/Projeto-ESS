import styles from "./index.module.css";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import Button from "../../components/buttom";
import Form from "../../components/Form";
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
                <Button value = "Boleto" onClick={handleBoletoClick}></Button>
                <Button value = "Cartão de débito" onClick={handleCartaoClick}></Button>
            </div>
            <div className={styles.container}>
                <Button value="Pix" onClick={handlePixClick}></Button>
            </div>
        </div>
        

    )

}


export default UpdatingMethod; 