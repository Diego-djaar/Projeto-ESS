import styles from "./index.module.css";
import Message from "../../Components/Message";
import SubmitButton from "../../Components/SubmitButton";
import Form from "../../Components/Form";
import ReturnButton from "../../Components/ReturnButton";
import { useNavigate } from 'react-router-dom';
import {useState} from 'react'
import axios from "axios";

const StoreSignUp = () => {

    const [nome, setNome] = useState("");
    const [cnpj, setCNPJ] = useState("");
    const [senha, setSenha] = useState("");
    const [categoria, setCategoria] = useState("");
    const [ email, setEmail] = useState("");
    const navigate = useNavigate(); 

    const StoreSingUphandler = (event) => {

        event.preventDefault();

        axios.post("http://127.0.0.1:8000/backend/api/store/signup", 
        {
            "CNPJ": cnpj,
            "Email": email,
            "Senha": senha,
            "Categoria": categoria,
            "Nome": nome,
        })
        .then(res => {if (res.data.message == "Já existe uma loja registrada com esses dados") {
            alert(`Já existe uma loja registrada com esses dados`)

    }})


    return (
        <div>
            <Message value="preencha com as suas informações"></Message>
            <form className={styles.forms}>
            <div>
            <Form Datacy = "inserir_nome_loja" placeholder= "Digite nome da loja"  onChange={event => 
            setNome(event.target.value)}></Form>  
            </div>
            <div>
            <Form Datacy = "inserir_cnpj_loja" placeholder= "Digite aqui o seu CNPJ"  onChange={event => 
            setCNPJ(event.target.value)}></Form>
            </div>
            <SubmitButton Datacy = "cadastrar loja" onClick = {event => StoreSingUphandler(event)} value = "Cadastrar"></SubmitButton>
            </form>
            <ReturnButton path="/paymentMethod/inserting"></ReturnButton>

        </div>
    )}
            }

export default StoreSignUp

