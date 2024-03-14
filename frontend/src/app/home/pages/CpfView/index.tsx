import styles from "./index.module.css";
import Pichu from "../../components/logo";
import SubmitButton from "../../components/SubmitButton";
import ReturnButton from "../../components/ReturnButton";
import Form from "../../components/Form";
import Message from "../../components/mensage";
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import axios from "axios";

const CPFView = () => {
    const [CPF, setCPF] = useState("");
    const [paymentData, setPaymentData] = useState([]);

    const handleClick = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.get(`http://127.0.0.1:8000/backend/api/payment/view/${CPF}`);
            if (response.data && response.data.data && response.data.data.res) {
                setPaymentData(response.data.data.res);
            } else {
                setPaymentData([]);
                alert("Nenhum método de pagamento retornado.");
            }
        } catch (error) {
            console.error('Erro ao buscar dados:', error);
            setPaymentData([]);
            alert("Erro ao buscar dados do servidor.");
        }
    }

    return (
        <div>
            <form action="">
                <Form
                    Datacy=""
                    placeholder="Insira o CPF"
                    onChange={e => setCPF(e.target.value)}
                />
                <SubmitButton
                    Datacy=""
                    value="Inserir"
                    onClick={e => handleClick(e)}
                />
                <ReturnButton path = "/PaymentMethod"></ReturnButton>
            </form>

            {paymentData.length > 0 && (
                <div>
                    <h2>Detalhes dos Métodos de Pagamento:</h2>
                    {paymentData.map((method, index) => (
                        <div key={index}>
                            {method.tipo === "pix" || method.tipo === "boleto" ? (
                                <div>
                                    <p>Nome: {method.nome_completo}</p>
                                    <p>Tipo: {method.tipo}</p>
                                    <p>ID: {method.id}</p>
                                </div>
                            ) : method.tipo === "cartao" && (
                                <div>
                                    <p>Nome: {method.nome_cartao}</p>
                                    <p>ID: {method.id}</p>
                                </div>
                            )}
                        </div>
                    ))}
                </div>
            )}
        </div>
    )
}

export default CPFView;
