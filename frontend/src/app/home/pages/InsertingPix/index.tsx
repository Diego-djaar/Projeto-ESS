import styles from "./index.module.css";
// import Button from "../../components/buttom";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
// import Formulario from "../../components/Formulário";
import { useNavigate } from 'react-router-dom';
import {useState} from 'react'
import axios from "axios";
// import axios from "axios";

const InsertingBoleto = () => {

    const [nome, setNomeCompleto] = useState("");
    const [cpf, setCpf] = useState("");
    const navigate = useNavigate(); 

    const insertBoletoHandler = (event) => {

        event.preventDefault();

        axios.post("http://127.0.0.1:8000/payment/inserting/pix", 
        {
            "nome_completo": nome,
            "cpf": cpf
        })
        .then(res => {if (res.data.message == "metodo de pagamento cadastrado com sucesso") {

            navigate("/paymentMethod/inserting")
            alert(res.data.message)
        }else if (res.data.message == "Já existe um pix cadastrado no sistema"){

            alert(res.data.message)

        }else {

            alert("Informações inválidas")

        } } )

    }

    return (
        <div>
            <Pichu></Pichu>
            <Message value="preencha com as suas informações"></Message>
            <div>
            <form className={styles.forms}>
            <label className={styles.label}>Nome completo</label>
            <input className = {styles.caixaTexto} type="text" placeholder="Digite aqui o seu nome completo" onChange={event => 
            setNomeCompleto(event.target.value)}/>
            <label className={styles.label}>CPF</label>
            <input className = {styles.caixaTexto} type="text" placeholder="Digite aqui o seu CPF" onChange={event => 
            setCpf(event.target.value)}/>
            <br />
            <button  className={styles.submissionButton} onClick = {event => insertBoletoHandler(event)}>Inserir pix</button>
            </form>
            </div>
    
        </div>
    )

}

export default InsertingBoleto
