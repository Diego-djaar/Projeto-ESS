import styles from "./index.module.css";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import SubmitButton from "../../components/SubmitButton";
import Form from "../../components/Form";
import ReturnButton from "../../components/ReturnButton";
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import axios from "axios";

const UpdatingPix = () => {
  const [id, setId] = useState(""); 
  const [novoNome, setNovoNome] = useState("");
  const navigate = useNavigate();  

  const handleUpdating = (e) => {
    e.preventDefault(); 

    axios.put(`http://127.0.0.1:8000/backend/api/payment/update/pix/${id}`, {
      "nome_completo": novoNome
    }).then(res => {
      if (res.data.message === "Dados atualizados com sucesso") {
        navigate("/paymentMethod/updating")
        alert("Dados atualizados com sucesso")
      } else {
        navigate("/paymentMethod/updating")
        alert("Id não encontrado")
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
          <Form Datacy = "update_id_pix" placeholder="Digite o ID do método" onChange={e => setId(e.target.value)}></Form>
        </div>
        <div>
          <Form Datacy="update_nome_pix" placeholder="Digite o novo nome" onChange={e => setNovoNome(e.target.value)}></Form>
        </div>
        <SubmitButton Datacy= "update_pix_botao" value="Atualizar" onClick={e => handleUpdating(e)}></SubmitButton>
        <ReturnButton path="/paymentMethod/updating"></ReturnButton>
    </form>
    </div>

  )
}

export default UpdatingPix;
