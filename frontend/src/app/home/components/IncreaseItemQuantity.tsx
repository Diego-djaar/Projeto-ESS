import React from 'react';
import axios, { AxiosError } from 'axios'; // Usando axios para chamadas HTTP
import styles from './IncreaseItemQuantity.module.css'

// ButtonProps.ts
interface ButtonProps {
    itemId: string;
    cpf: string;
    onItemIncreaseQuantity: () => void; // Esta função será chamada após a remoção bem-sucedida
    onError: (message: string) => void; // Esta função será chamada em caso de erro
  }  

const IncreaseItemQuantityButton: React.FC<ButtonProps> = ({ itemId, cpf, onItemIncreaseQuantity, onError }) => {
  const increaseQuantity = async () => {
    try {
      // Atenção: Os parâmetros devem ser enviados como query string na URL
      const response = await axios.put(`http://127.0.0.1:8000/backend/api/carrinho/incrementar_item?item_id=${itemId}&CPF=${cpf}`);

      if (response.status === 200) {
        onItemIncreaseQuantity(); // Chamar o callback de sucesso
      } else {
        onError('Falha ao incrementar a quantidade do item'); // Chamar o callback de erro
      }
    } catch (error) {
      let errorMessage = 'Erro desconhecido';
      if (axios.isAxiosError(error)) {
        if (error.response) {
          // Resposta com erro da API
          errorMessage = error.response.data.detail || error.response.statusText;
        } else if (error.request) {
          // O erro ocorreu na configuração da requisição e a requisição foi enviada,
          // mas não houve resposta do servidor
          errorMessage = 'Nenhuma resposta foi recebida do servidor.';
        } else {
          // Um erro ocorreu ao configurar a requisição que disparou um erro
          errorMessage = error.message;
        }
      }
      onError(errorMessage);
      console.error(error);
    }
  };

  return (
    <button className={styles.quantityPlus} onClick={increaseQuantity}>
      +
    </button>
  );
};


export default IncreaseItemQuantityButton;
