import styles from "./index.module.css";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import Form from "../../components/Form";
import { useNavigate } from 'react-router-dom';
import {useState} from 'react'
import axios from "axios";
import SubmitButton from "../../components/SubmitButton";


const InsertingCard = () => {

    const [nome, setNome] = useState("");
    const [numero, setNumero] = useState("");
    const [cvv, setCvv] = useState("");
    const [cpf, setCpf] = useState("");
    const [validade, setValidade] = useState("");
    const navigate = useNavigate(); 

    const insertCartaoHandler = (event) => {

        event.preventDefault();

        axios.post("http://127.0.0.1:8000/backend/api/payment/inserting/cartao", 
        {
            "nome_cartao": nome,
            "numero_cartao": numero,
            "cvv": cvv,
            "cpf": cpf,
            "validade":validade,
              
        })
        .then(res => {if (res.data.message == "metodo de pagamento cadastrado com sucesso") {

            navigate("/paymentMethod/inserting")
            alert(res.data.message)
        }else {

            alert("Informações inválidas")

        } } )

    }

    return (
        <div>
            <Pichu></Pichu>
            <Message value="preencha com as suas informações"></Message>
            <form action="">
                <div className={styles.container1}>
                <Form placeholder="Digite o nome" onChange={e => setNome(e.target.value)}></Form>
                <Form placeholder="Digite o número" onChange={e => setNumero(e.target.value)}></Form>
                </div>
                <div className={styles.container2}>
                <Form placeholder="Digite o CVV" onChange={e => setCvv(e.target.value)}></Form>
                <Form placeholder="Digite o seu CPF" onChange={e => setCpf(e.target.value)}></Form>
                </div>
                <div className={styles.container3}>
                <Form placeholder="Digite a validade do cartão" onChange={e => setValidade(e.target.value)}></Form>
                </div>
                <div className={styles.container4}>
                 <SubmitButton value= "Inserir cartão" onClick = {event => insertCartaoHandler(event)}></SubmitButton>
                </div>
            </form>
        </div>
    )

}

export default InsertingCard 
