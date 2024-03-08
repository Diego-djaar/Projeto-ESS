import { useState } from 'react';
import ItemData from '../models/ItemData';
import HTTPResponseData from '../models/HTTPResponseData';

function GetCart() {
  const [cpf, setCpf] = useState('');
  const [responseData, setResponseData] = useState<HTTPResponseData | null>(null);
  const [error, setError] = useState('');

  const handleInputChange = (event) => {
    setCpf(event.target.value);
  };

  const handleButtonClick = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/backend/api/carrinho/view/${cpf}`);
      if (!response.ok) {
        throw new Error('Falha na obtenção do conteúdo do carrinho');
      }
      const data = await response.json();
      setResponseData(data);
      setError('');
    } catch (error) {
      console.error(error);
      setError('Falha na obtenção do conteúdo do carrinho');
    }
  };

  return (
    <div>
      <h1>Visualização do Carrinho</h1>
      <input
        type="text"
        value={cpf}
        onChange={handleInputChange}
        placeholder="Digite o CPF"
      />
      <button onClick={handleButtonClick}>Visualizar Carrinho</button>
      {error && <p>{error}</p>}
      {responseData && responseData.data && (
        <div>
          <h2>Status: {responseData.status_code}</h2>
          <p>Mensagem: {responseData.message}</p>
          <p>Itens:</p>
          <ul>
            {responseData.data.Itens.map((item: ItemData, index) => (
              <li key={index}>
                <div>
                  <p>ID: {item.id}</p>
                  <p>Nome: {item.nome}</p>
                  <p>Descrição: {item.description}</p>
                  <p>Preço: {item.price}</p>
                  <p>Quantidade: {item.quantidade}</p>
                  {item.img && <img src={item.img} alt={item.nome} />}
                </div>
              </li>
            ))}
          </ul>
          <p>Total: {responseData.data.Total}</p>
          <p>Endereço: {responseData.data.Endereço}</p>
        </div>
      )}
    </div>
  );
}

export default GetCart;
