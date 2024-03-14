import React from 'react';
import axios from 'axios'; // Usando axios para chamadas HTTP
import "./RemoveFromCartButton.css"

// ButtonProps.ts
interface ButtonProps {
    itemId: string;
    cpf: string;
    onItemRemoved: () => void; // Esta função será chamada após a remoção bem-sucedida
    onError: (message: string) => void; // Esta função será chamada em caso de erro
  }  

const RemoveFromCartButton: React.FC<ButtonProps> = ({ itemId, cpf, onItemRemoved, onError }) => {
  const removeFromCart = async () => {
    try {
      // Chamar a API para remover o item do carrinho
      const response = await axios.delete(`http://127.0.0.1:8000/backend/api/carrinho/remover`, {
        params: { item_id: itemId, CPF: cpf },
      });

      if (response.status === 200) {
        onItemRemoved(); // Chamar o callback de sucesso
      } else {
        onError('Falha na remoção do item do carrinho'); // Chamar o callback de erro
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
    <button className="removeButton" onClick={removeFromCart}>
      Remover
    </button>
  );
};

export default RemoveFromCartButton;
