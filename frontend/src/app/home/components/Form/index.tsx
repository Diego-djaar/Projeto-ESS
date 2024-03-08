import styles from "./index.module.css";
// import Button from "../../components/buttom";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
// import Formulario from "../../components/Formulário";
import { useNavigate } from 'react-router-dom';
import {useState} from 'react'
import axios from "axios";

const Form = ({placeholder, onChange}) => {

    return (
        <>
        <input type="text" className={styles.caixaTexto} placeholder={placeholder}  onChange={onChange}/>
        </>
    )

}

export default Form;
