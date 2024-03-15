import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './basic.css';


function Inventory() {
  const [cnpj, setCnpj] = useState('');
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState('');
  const [inventoryItems, setInventoryItems] = useState([]);

  useEffect(() => {
    if (responseData && responseData.data) {
      setInventoryItems(responseData.data.map(item => ({ itemId: item.id_item, qnt: 0 })));
    }
  }, [responseData]);

  const handleInputChange = (event) => {
    setCnpj(event.target.value);
  };

  const handleButtonClick = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/backend/api/inventory/${cnpj}`);
      if (!response.ok) {
        throw new Error('Falha na obtenção do conteúdo do inventário');
      }
      const data = await response.json();
      setResponseData(data);
      setError('');
    } catch (error) {
      console.error(error);
      setError('Falha na obtenção do conteúdo do inventário');
    }
  };

  const handleUpdateButtonClick = async (itemId, qnt) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/backend/api/inventory/${cnpj}/atualizar_estoque?item_id=${itemId}&qnt=${qnt}`, {
        method: 'POST',
      });
      if (!response.ok) {
        throw new Error('Falha na atualização do inventário');
      }

      // Refresh the inventory after updating
      handleButtonClick();
    } catch (error) {
      console.error(error);
      console.log(error);
      setError('Falha na atualização do inventário');
    }
  };

  const handleQuantityChange = (itemId, qnt) => {
    setInventoryItems(prevItems => {
      return prevItems.map(item => {
        if (item.itemId === itemId) {
          return { ...item, qnt };
        }
        return item;
      });
    });
  };

  return (
    <div>
      <h1>Visualização do Inventário</h1>
      <input
        type="text"
        value={cnpj}
        onChange={handleInputChange}
        placeholder="Digite o CNPJ"
      />
      <button onClick={handleButtonClick}>Visualizar Inventário</button>
{error && <p>{error}</p>}
{responseData && responseData.status_code === 200 ? (
  <div>
      <InventoryList
        responseData={responseData}
        inventoryItems={inventoryItems}
        handleQuantityChange={handleQuantityChange}
        handleUpdateButtonClick={handleUpdateButtonClick}
      />
      <AddItemButton cnpj={cnpj} /> 
  </div>
) : responseData && responseData.status_code === 404 ? (
  <div>
  <p>Lista vazia</p>
  <AddItemButton cnpj={cnpj} /> 
  </div>
) : null}
    </div>
  );
}

export default Inventory;


export const InventoryList = ({ responseData, inventoryItems, handleQuantityChange, handleUpdateButtonClick }) => {
  return (
    <div>
    <h2>Status: {responseData.status_code}</h2>
    <p>Mensagem: {responseData.message}</p>
    <p>Itens:</p>
    <ul>
      {responseData.data.map((item, index) => (
        <li key={index}>
          <div>
            <p>ID: {item.id_item}</p>
            <p>Nome: {item.nome}</p>
            <p>Quantidade: {item.qnt}</p>
            <input
              type="number"
              value={inventoryItems.find(invItem => invItem.itemId === item.id_item)?.qnt || ''}
              onChange={(e) => handleQuantityChange(item.id_item, parseInt(e.target.value))}
            />
            <button onClick={() => handleUpdateButtonClick(item.id_item, inventoryItems.find(invItem => invItem.itemId === item.id_item)?.qnt)}>Update Quantity</button>
          </div>
        </li>
      ))}
    </ul>
    </div>
  );
};

export const AddItemButton = ({ cnpj }) => {
  return (
    <Link to={`/inventory/add_item/${cnpj}`}>
      <button>Add Item</button>
    </Link>
  );
};
