import React, { useState } from 'react';
import ItemData from '../models/ItemData';
import HTTPResponseData from '../models/HTTPResponseData';
import ItemComponent from './Item';
import styles from './getCart.module.css';
import { useCpf } from '../context/HomeContext/CpfContext';
import AdressComponent from './AdressComponent';

function GetCart() {
  const [responseData, setResponseData] = useState<HTTPResponseData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [cpf, setCpf] = useCpf();

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setCpf(event.target.value);
  };

  const handleRefreshCart = async () => {
    // Apenas chame loadCart sem definir estado adicional, já que loadCart já define estados.
    await loadCart();
  };

  // Função para carregar o carrinho de compras
  const loadCart = async () => {
    setLoading(true);
    try {
      const response = await fetch(`http://127.0.0.1:8000/backend/api/carrinho/view/${cpf}`);
      if (!response.ok) {
        throw new Error('Falha na obtenção do conteúdo do carrinho');
      }
      const data = await response.json();
      setResponseData(data);
      setError(''); // Limpe o erro se houver um sucesso
    } catch (error) {
      setError('Falha na obtenção do conteúdo do carrinho');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  // Esta função agora será usada no botão e após alterações nos itens.
  const handleViewCartClick = () => {
    handleRefreshCart();
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
        disabled={loading}
      />
      <button
        className={styles.viewCartButton}
        onClick={handleViewCartClick}
        disabled={loading}
      >
        {loading ? 'Carregando...' : 'Visualizar Carrinho'}
      </button>
      {error && <p className={styles.errorMsg}>{error}</p>}
      {responseData && responseData.data && (
        <div className={styles.cartDetails}>
          <h2 className={styles.statusMessage}>Status: {responseData.status_code}</h2>
          <p className={styles.statusMessage}>Mensagem: {responseData.message}</p>
          {loading ? (
            <p className={styles.statusMessage}>Atualizando itens...</p>
          ) : (
            <>
              <p className={styles.statusMessage}>Itens:</p>
              <ul className={styles.itemList}>
                {responseData.data.Itens.map((item: ItemData) => (
                  <li key={item.id}>
                    <ItemComponent
                      item={item}
                      onItemChange={handleRefreshCart}
                    />
                  </li>
                ))}
              </ul>
              <p className={styles.totalPrice}>Total: {responseData.data.Total}</p>
              <AdressComponent endereco_atual={responseData.data.Endereço} />
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default GetCart;
