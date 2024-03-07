import styles from "./index.module.css";
import Button from "../../components/buttom";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import Formulario from "../../components/Formulário";
import { useNavigate } from 'react-router-dom';


const InsertingBoleto = () => {

    return (
        <div>
            <Pichu></Pichu>
            <Message value="preencha com as suas informações "></Message>
            <Formulario label="Nome completo"></Formulario>
            <Formulario label="CPF"></Formulario>
        </div>
    )

}

export default InsertingBoleto
