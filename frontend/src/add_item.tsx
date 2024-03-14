import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';
import './basic.css';



function generateRandomNumber() {
  // Generate a random decimal number between 0 and 1
  const randomDecimal = Math.random();

  // Multiply the random decimal by 10^8 (100,000,000) to get an 8-digit number
  const randomNumber = Math.floor(randomDecimal * 100000000);

  return randomNumber;
}

function AddItem() {
  const [nome, setNome] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [quantidade, setQuantidade] = useState('');
  const [img, setImg] = useState('');
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const { CNPJ } = useParams();

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const codigo = generateRandomNumber();

      const response = await fetch(`http://127.0.0.1:8000/backend/api/inventory/${CNPJ}/adicionar_item?id=${codigo}&nome=${nome}&description=${description}&price=${price}&quantidade=${quantidade}`, {
        method: 'POST',
      });

      const data = await response.json(); // Parse response JSON data

      // If response is not OK, throw an error
      if (!response.ok) {        
        throw new Error(response.statusText); // Use the message returned from the server
      }

      // Clear form fields on successful submission
      setNome('');
      setDescription('');
      setPrice('');
      setQuantidade('');
      setImg('');
      setError('');
      setSuccessMessage('Item adicionado com sucesso'); // Set success message
    } catch (error) {
      // Handle errors
      console.error(error);
      console.log(error);
      setError(error.message); // Set error message
    }
  };

  return (
    <div>
      <h2>Adicionar Novo Item</h2>
      {error && <p className = "error">{error}</p>}
      {successMessage && <p className="success">{successMessage}</p>}
      <form onSubmit={handleSubmit}>
        <label>
          Nome:
          <input type="text" value={nome} onChange={(e) => setNome(e.target.value)} required />
        </label>
        <br />
        <label>
          Descrição:
          <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} required />
        </label>
        <br />
        <label>
          Preço:
          <input type="text" value={price} onChange={(e) => setPrice(e.target.value)} required />
        </label>
        <br />
        <label>
          Quantidade:
          <input type="number" value={quantidade} onChange={(e) => setQuantidade(e.target.value)} required />
        </label>
        <br />
        <label>
          Imagem:
          <input type="text" value={img} onChange={(e) => setImg(e.target.value)} />
        </label>
        <br />
        <button type="submit">Adicionar Item</button>
      </form>
    	<Link to={`/inventory`}><button>Voltar</button></Link>
    </div>
  );
}

export default AddItem;
