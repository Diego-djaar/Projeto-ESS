import { useState } from 'react';
import ItemData from '../models/ItemData';
import HTTPResponseData from '../models/HTTPResponseData';
import ItemComponent from './Item';
import styles from './getCart.module.css'

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
    <div className={styles.container}>
      <h1 className={styles.header}>Visualização do Carrinho</h1>
      <input
        className={styles.inputCpf}
        type="text"
        value={cpf}
        onChange={handleInputChange}
        placeholder="Digite o CPF"
      />
      <button
        className={styles.viewCartButton}
        onClick={handleButtonClick}
      >
        Visualizar Carrinho
      </button>
      {error && <p className={styles.errorMsg}>{error}</p>}
      {responseData && responseData.data && (
        <div className={styles.cartDetails}>
          <h2 className={styles.statusMessage}>Status: {responseData.status_code}</h2>
          <p className={styles.statusMessage}>Mensagem: {responseData.message}</p>
          <p className={styles.statusMessage}>Itens:</p>
          <ul className={styles.itemList}>
            {responseData.data.Itens.map((item: ItemData, index) => (
              <li key={index}>
                <ItemComponent item={item} />
              </li>
            ))}
          </ul>
          <p className={styles.totalPrice}>Total: {responseData.data.Total}</p>
          <p className={styles.addressInfo}>Endereço: {responseData.data.Endereço}</p>
        </div>
      )}
    </div>
  );
}

export default GetCart;
