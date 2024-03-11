import styles from "./index.module.css";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import Form from "../../components/Form";
import ReturnButton from "../../components/ReturnButton";
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
            alert(`metodo de pagamento cadastrado com sucesso`)
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
                <Form Datacy= "inserir_nome_cartao" placeholder="Digite o nome" onChange={e => setNome(e.target.value)}></Form>
                <Form Datacy= "inserir_numero_cartao" placeholder="Digite o número" onChange={e => setNumero(e.target.value)}></Form>
                </div>
                <div className={styles.container2}>
                <Form Datacy="inserir_cvv" placeholder="Digite o CVV" onChange={e => setCvv(e.target.value)}></Form>
                <Form Datacy="inserir_cpf_cartao" placeholder="Digite o seu CPF" onChange={e => setCpf(e.target.value)}></Form>
                </div>
                <div className={styles.container3}>
                <Form Datacy="inserir_validade" placeholder="Digite a validade do cartão" onChange={e => setValidade(e.target.value)}></Form>
                </div>
                <div className={styles.container4}>
                 <SubmitButton Datacy="inserir_cartao_botao" value= "Inserir cartão" onClick = {event => insertCartaoHandler(event)}></SubmitButton>
                </div>
                <ReturnButton path="/paymentMethod/inserting"></ReturnButton>
            </form>
        </div>
    )

}

export default InsertingCard 
