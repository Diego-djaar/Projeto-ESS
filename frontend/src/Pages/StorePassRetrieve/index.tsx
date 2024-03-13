import styles from "./index.module.css";
import Message from "../../Components/Message";
import SubmitButton from "../../Components/SubmitButton";
import Form from "../../Components/Form";
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import axios from "axios";

const StoreRetrieve = () => {

    const [cnpj, setCNPJ] = useState("");
    const [senha, setSenha] = useState("");
    const [email, setEmail] = useState("");
    const navigate = useNavigate();

    const StoreRetrievehandler = (event) => {
        event.preventDefault();

        axios.post("http://127.0.0.1:8000/backend/api/stores/login/retrieve_password", 
        {
            "cnpj": cnpj,
            "email": email,
            "senha": senha,
        })
        .then(res => {
            if (res.data.message === "CNPJ ou Email incorretos") {
                alert(res.data.message);
            }
            else if (res.data.message == "Não tem autorização para realizar essa requisição"){
                alert(res.data.message)
    
            }
            else if (res.data.message == "Atualização de dados bem sucedida"){
                alert(res.data.message)
    
            }
        });
    };

    return (
        <div>
            <Message value="preencha com as suas informações"></Message>
            <form className={styles.forms}>
                <div>
                    <Form Datacy="inserir_cnpj_loja" placeholder="Digite aqui o seu CNPJ" onChange={event => 
                    setCNPJ(event.target.value)}></Form>
                </div>
                <div>
                    <Form Datacy="inserir_cnpj_loja" placeholder="Digite aqui sua nova senha" onChange={event => 
                    setSenha(event.target.value)}></Form>
                </div>
                <div>
                    <Form Datacy="inserir_cnpj_loja" placeholder="Digite aqui o seu email" onChange={event => 
                    setEmail(event.target.value)}></Form>
                </div>
                <SubmitButton Datacy="cadastrar_loja" onClick={event => StoreRetrievehandler(event)} value="Recupera senha"></SubmitButton>
            </form>
        </div>
    );
};

export default StoreRetrieve;
