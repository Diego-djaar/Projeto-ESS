import styles from "./index.module.css";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import SubmitButton from "../../components/SubmitButton";
import Form from "../../components/Form";
import { useNavigate } from 'react-router-dom';
import ReturnButton from "../../components/ReturnButton";
import { useState } from 'react';
import axios from "axios";

const UpdatingBoleto = () => {
  const [id, setId] = useState(""); 
  const [novoNome, setNovoNome] = useState("");
  const navigate = useNavigate();  

  const handleUpdating = (e) => {
    e.preventDefault(); 

    console.log(id)
    console.log(novoNome)

    const path = `http://127.0.0.1:8000/backend/api/payment/update/boleto/${id}`; 
    console.log(path)

    axios.put(`http://127.0.0.1:8000/backend/api/payment/update/boleto/${id}`, {
      "nome_completo": novoNome
    }).then(res => {
      if (res.data.message === "Dados atualizados com sucesso") {
        alert("Dados atualizados com sucesso")
        navigate("/paymentMethod/updating")
      } else {
        alert("Id não encontrado")
        navigate("/paymentMethod/updating")
      }
    }).catch(error => {
      // Lida com erros, se houver algum
      console.error('Erro ao fazer a solicitação POST:', error);
    });
  }

  return (
    <div>
        <Pichu></Pichu>
        <Message value="Preecha com as informações"></Message>
        <form action="" className={styles.forms}>
        <div>
          <Form Datacy = "update_id_boleto" placeholder="Digite o ID do método" onChange={e => setId(e.target.value)}></Form>
        </div>
        <div>
          <Form Datacy = "update_nome_boleto" placeholder="Digite o novo nome" onChange={e => setNovoNome(e.target.value)}></Form>
        </div>
        <SubmitButton Datacy = "update_boleto_botao" value="Atualizar" onClick={e => handleUpdating(e)}></SubmitButton>
    </form>
    <ReturnButton path = "/paymentMethod/updating"></ReturnButton>
    </div>

  )
}

export default UpdatingBoleto;
