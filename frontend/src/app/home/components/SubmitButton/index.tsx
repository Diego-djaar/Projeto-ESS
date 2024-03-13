import styles from "./index.module.css";
// import Button from "../../components/buttom";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import Form from "../../components/Form";
// import Formulario from "../../components/Formulário";
import { useNavigate } from 'react-router-dom';
import {useState} from 'react'
import axios from "axios";
// import axios from "axios";

const SubmitButton = ({onClick, value, Datacy}) => {

    return (
        <>  
        <button data-cy = {Datacy} className={styles.submissionButton} onClick = {onClick}>{value}</button>   
        </>
    )

}

export default SubmitButton; 