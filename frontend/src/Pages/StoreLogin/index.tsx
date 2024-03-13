import styles from "./index.module.css";
import Message from "../../Components/Message";
import SubmitButton from "../../Components/SubmitButton";
import Form from "../../Components/Form";
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import axios from "axios";

const StoreLogin = () => {

    const [cnpj, setCNPJ] = useState("");
    const [senha, setSenha] = useState("");
    const navigate = useNavigate();

    const StoreLoginhandler = (event) => {
        event.preventDefault();

        axios.post("http://127.0.0.1:8000/backend/api/stores/login", 
        {
            "cnpj": cnpj,
            "senha": senha,
        })
        .then(res => {
            if (res.data.message === "CNPJ ou Senha incorretos") {
                alert(res.data.message);
            }
            else if (res.data.message == "Login com sucesso"){
                //navigate("/stores/homepage")
                alert(res.data.message)
    
            }
            else if (res.data.message == "Login falhou, essa loja não deve estar cadastrada"){
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
                    <Form Datacy="inserir_senha_loja" placeholder="Digite aqui o sua senha" onChange={event => 
                    setSenha(event.target.value)}></Form>
                </div>
                
                <SubmitButton Datacy="login_loja" onClick={event => StoreLoginhandler(event)} value="Login"></SubmitButton>
            </form>
        </div>
    );
};

export default StoreLogin;
