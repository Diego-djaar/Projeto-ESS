import React from 'react';
import axios from 'axios'; // Usando axios para chamadas HTTP
import styles from "./AddToCartButton.module.css"
import ItemData from '../models/ItemData';

// ButtonProps.ts
interface ButtonProps {
    item: ItemData;
    cpf: string;
    onItemAdded: () => void; // Esta função será chamada após a adição bem-sucedida
    onError: (message: string) => void; // Esta função será chamada em caso de erro
  }  

const AddToCartButton: React.FC<ButtonProps> = ({ item, cpf, onItemAdded, onError }) => {
  const addToCart = async () => {
    try {
      // Chamar a API para adicionar o item ao carrinho
      const response = await axios.post(`http://127.0.0.1:8000/backend/api/carrinho/adicionar?CPF=${cpf}`, item);

      if (response.status === 200) {
        onItemAdded(); // Chamar o callback de sucesso
      } else {
        onError('Falha na adição do item ao carrinho'); // Chamar o callback de erro
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
    <button className={styles.itemAddButton} onClick={addToCart}>
      Adicionar ao carrinho
    </button>
  );
};

export default AddToCartButton;
