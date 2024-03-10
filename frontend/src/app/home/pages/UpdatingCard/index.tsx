import styles from "./index.module.css";
import Pichu from "../../components/logo";
import Message from "../../components/mensage";
import SubmitButton from "../../components/SubmitButton";
import Form from "../../components/Form";
import ReturnButton from "../../components/ReturnButton";
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import axios from "axios";

const UpdatingCartao = () => {
    const [id, setId] = useState("");
    const [nomeCartao, setNomeCartao] = useState("");
    const [numeroCartao, setNumeroCartao] = useState("");
    const [cvv, setCvv] = useState("");
    const [validade, setValidade] = useState("");
    const navigate = useNavigate();  

  const handleUpdating = (e) => {

    e.preventDefault(); 

    axios.put(`http://127.0.0.1:8000/backend/api/payment/update/cartao/${id}`, {
        "nome_cartao": nomeCartao,
        "numero_cartao": numeroCartao,
        "cvv": cvv,
        "validade": validade
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
          <Form placeholder="Digite o ID do método" onChange={e => setId(e.target.value)}></Form>
        </div>
        <div>
          <Form placeholder="Digite o novo nome do cartão" onChange={e => setNomeCartao(e.target.value)}></Form>
          <Form placeholder="Digite o novo numero do cartão" onChange={e => setNumeroCartao(e.target.value)}></Form>
        </div>
        <div>
          <Form placeholder="Digite o novo cvv" onChange={e => setCvv(e.target.value)}></Form>
          <Form placeholder="Digite a nova validade" onChange={e => setValidade(e.target.value)}></Form>
        </div>
        <SubmitButton value="Atualizar" onClick={e => handleUpdating(e)}></SubmitButton>
        <ReturnButton path = "/paymentMethod/updating"></ReturnButton>
    </form>
    </div>

  )
}

export default UpdatingCartao;
