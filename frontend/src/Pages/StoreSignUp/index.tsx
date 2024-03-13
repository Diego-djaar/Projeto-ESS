import styles from "./index.module.css";
import Message from "../../Components/Message";
import SubmitButton from "../../Components/SubmitButton";
import Form from "../../Components/Form";
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import axios from "axios";

const StoreSignUp = () => {

    const [nome, setNome] = useState("");
    const [cnpj, setCNPJ] = useState("");
    const [senha, setSenha] = useState("");
    const [categoria, setCategoria] = useState("");
    const [email, setEmail] = useState("");
    const navigate = useNavigate();

    const StoreSingUphandler = (event) => {
        event.preventDefault();

        axios.post("http://127.0.0.1:8000/backend/api/stores/signup", 
        {
            "cnpj": cnpj,
            "email": email,
            "senha": senha,
            "categoria": categoria,
            "nome": nome,
        })
        .then(res => {
            if (res.data.message === "Já existe uma loja registrada com esses dados") {
                alert(res.data.message);
            }
            else if (res.data.message == "Já existe uma loja registrada com esses dados"){
                navigate("/stores/login")
                alert(res.data.message)
    
            }
        });
    };

    return (
        <div>
            <Message value="preencha com as suas informações"></Message>
            <form className={styles.forms}>
                <div>
                    <Form Datacy="inserir_nome_loja" placeholder="Digite nome da loja" onChange={event => 
                    setNome(event.target.value)}></Form>  
                </div>
                <div>
                    <Form Datacy="inserir_cnpj_loja" placeholder="Digite aqui o seu CNPJ" onChange={event => 
                    setCNPJ(event.target.value)}></Form>
                </div>
                <div>
                    <Form Datacy="inserir_cnpj_loja" placeholder="Digite aqui o sua senha" onChange={event => 
                    setSenha(event.target.value)}></Form>
                </div>
                <div>
                    <Form Datacy="inserir_cnpj_loja" placeholder="Digite aqui o sua categoria" onChange={event => 
                    setCategoria(event.target.value)}></Form>
                </div>
                <div>
                    <Form Datacy="inserir_cnpj_loja" placeholder="Digite aqui o seu email" onChange={event => 
                    setEmail(event.target.value)}></Form>
                </div>
                <SubmitButton Datacy="cadastrar_loja" onClick={event => StoreSingUphandler(event)} value="Cadastrar"></SubmitButton>
            </form>
        </div>
    );
};

export default StoreSignUp;
