import styles from "./index.module.css";
import Pichu from "../../components/logo";
import SubmitButton from "../../components/SubmitButton";
import ReturnButton from "../../components/ReturnButton";
import Form from "../../components/Form";
import Message from "../../components/mensage";
import { useNavigate } from 'react-router-dom';
import {useState} from 'react'
import axios from "axios";


const InsertingBoleto = () => {

    const [nome, setNomeCompleto] = useState("");
    const [cpf, setCpf] = useState("");
    const navigate = useNavigate(); 

    const insertBoletoHandler = (event) => {

        event.preventDefault();

        axios.post("http://127.0.0.1:8000/backend/api/payment/inserting/boleto", 
        {
            "nome_completo": nome,
            "cpf": cpf
        })
        .then(res => {if (res.data.message == "metodo de pagamento cadastrado com sucesso") {

            navigate("/paymentMethod/inserting")
            alert(`metodo de pagamento cadastrado com sucesso\nSeu ID é ${res.data.data["ID"]}`)
        }else if (res.data.message == "Já existe um boleto cadastrado no sistema"){

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
            <Form Datacy = "inserir_nome_boleto" placeholder="Digite aqui o seu nome completo" onChange={event => 
            setNomeCompleto(event.target.value)}></Form>  
            </div>  
            <div>
            <Form Datacy = "inserir_cpf_boleto" placeholder="Digite aqui o seu CPF"  onChange={event => 
            setCpf(event.target.value)}></Form>    
            </div>
            <SubmitButton Datacy = "inserir_boleto_botao" value = "Inserir Boleto" onClick = {event => insertBoletoHandler(event)}></SubmitButton> 
            <ReturnButton path="/paymentMethod/inserting"></ReturnButton>
            </form>
            </div>
    
        </div>
    )

}

export default InsertingBoleto
