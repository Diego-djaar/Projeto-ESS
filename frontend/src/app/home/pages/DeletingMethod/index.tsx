import styles from "./index.module.css";
import Pichu from "../../components/logo";
import SubmitButton from "../../components/SubmitButton";
import ReturnButton from "../../components/ReturnButton";
import Form from "../../components/Form";
import Message from "../../components/mensage";
import { useNavigate } from 'react-router-dom';
import {useState} from 'react'
import axios from "axios";


const DeletingMethod = () => {

    const [id, setId] = useState("");    
    const navigate = useNavigate(); 

    const insertBoletoHandler = (event) => {

        event.preventDefault();

        axios.delete(`http://127.0.0.1:8000/backend/api/payment/delete/${id}`)
        .then(res => {if (res.data.message == "Deleção realizada com sucesso") {

            navigate("/paymentMethod/inserting")
            alert(res.data.message)
        }else if (res.data.message == "ID não encontrado na base de dados"){

            alert(res.data.message)

        }else {

            alert("Informações inválidas")

        } } )

    }

    return (
        <div>
            <Pichu></Pichu>
            <Message value="preencha com as suas informações"></Message>
            <div>
            <form className={styles.forms}>
            <div>
            <Form Datacy="delete_id" placeholder="Digite aqui o Id do método a ser deletado" onChange={event => 
            setId(event.target.value)}></Form>  
            </div>  
            <SubmitButton Datacy="delete_button" value = "Deletar" onClick = {event => insertBoletoHandler(event)}></SubmitButton>            
            </form>
            </div>
            <ReturnButton path="/paymentMethod"></ReturnButton>
    
        </div>
    )

}

export default DeletingMethod
