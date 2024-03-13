import styles from "./index.module.css";
import Message from "../../Components/Message";
import SubmitButton from "../../Components/SubmitButton";
import Form from "../../Components/Form";
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import axios from "axios";

const StoreUpdate = () => {

    const [nnome, setNome] = useState("");
    const [cnpj, setCNPJ] = useState("");
    const [senha, setSenha] = useState("");
    const [nsenha, setnSenha] = useState("");
    const [ncategoria, setCategoria] = useState("");
    const [nemail, setEmail] = useState("");
    const navigate = useNavigate();

    const StoreUpdatehandler = (event) => {
        event.preventDefault();

        axios.post("http://127.0.0.1:8000/backend/api/stores/login", 
        {
            "cnpj": cnpj,
            "nemail": nemail,
            "senha": senha,
            "nsenha": nsenha,
            "ncategoria": ncategoria,
            "nnome": nnome,
        })
        .then(res => {
            if (res.data.message === "CNPJ ou Email incorretos") {
                alert(res.data.message);
            }
            else if (res.data.message == "Não tem autorização para realizar essa requisição"){
                //navigate("/stores/homepage")
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
                    <Form Datacy="inserir_senha_loja" placeholder="Digite aqui a sua senha" onChange={event => 
                    setSenha(event.target.value)}></Form>
                </div>
                <div>
                    <Form Datacy="inserir_nemail_loja" placeholder="Digite aqui seu novo email" onChange={event => 
                    setEmail(event.target.value)}></Form>
                </div>
                <div>
                    <Form Datacy="inserir_nsenha_loja" placeholder="Digite aqui sua nova senha" onChange={event => 
                    setnSenha(event.target.value)}></Form>
                </div>
                <div>
                    <Form Datacy="inserir_ncategoria_loja" placeholder="Digite aqui sua nova categoria" onChange={event => 
                    setCategoria(event.target.value)}></Form>
                </div>
                <div>
                    <Form Datacy="inserir_nnome_loja" placeholder="Digite aqui seu novo nome" onChange={event => 
                    setNome(event.target.value)}></Form>
                </div>
                
                <SubmitButton Datacy="login_loja" onClick={event => StoreUpdatehandler(event)} value="Update"></SubmitButton>
            </form>
        </div>
    );
};

export default StoreUpdate;
