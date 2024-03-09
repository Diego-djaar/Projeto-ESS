import React, { useState, useEffect } from 'react';
import ItemData from '../models/ItemData';
import HTTPResponseData from '../models/HTTPResponseData';
import ItemComponent from './Item';
import styles from './getCart.module.css';
import { useCpf } from '../context/HomeContext/CpfContext';

function GetCart() {
  const [responseData, setResponseData] = useState<HTTPResponseData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [cpf, setCpf] = useCpf();

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
    } catch (error) {
      setError('Falha na obtenção do conteúdo do carrinho');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  // Efeito para carregar o carrinho na montagem do componente
  useEffect(() => {
    loadCart();
  }, [cpf]);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setCpf(event.target.value);
  };

  const handleRefreshCart = () => {
    loadCart(); // Recarrega o carrinho após uma ação do usuário
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
        onClick={loadCart}
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
              <p className={styles.addressInfo}>Endereço: {responseData.data.Endereço}</p>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default GetCart;
