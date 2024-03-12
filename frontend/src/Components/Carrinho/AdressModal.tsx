import './AdressModal.css';

const AdressModal = ({ endereco, setEndereco, onSubmit, onClose, errorMessage }) => {

  const handleChange = (event) => {
    const { name, value } = event.target;
    setEndereco(prevEndereco => ({
      ...prevEndereco,
      [name]: name === 'numero' ? Number(value) : value
    }));
  };

  return (
    <div className="modalBackground">
      <div className="modalContainer">
        <div className="modalHeader">
          <h2>Editar Endereço</h2>
          <button onClick={onClose} className="closeButton">&times;</button>
        </div>
        <div className="modalContent">
          <input name="rua" value={endereco.rua} onChange={handleChange} placeholder="Rua *" />
          <input name="numero" type="number" value={endereco.numero} onChange={handleChange} placeholder="Número *" />
          <input name="bairro" value={endereco.bairro} onChange={handleChange} placeholder="Bairro *" />
          <input name="cidade" value={endereco.cidade} onChange={handleChange} placeholder="Cidade *" />
          <input name="estado" value={endereco.estado} onChange={handleChange} placeholder="Estado *" />
          <input name="cep" value={endereco.cep} onChange={handleChange} placeholder="CEP *" />
          <input name="pais" value={endereco.pais} onChange={handleChange} placeholder="País *" />
          <input name="complemento" value={endereco.complemento || ''} onChange={handleChange} placeholder="Complemento" />
        </div>
        <div className="modalActions">
          <button onClick={onSubmit} className="saveButton">Salvar Endereço</button>
          <button onClick={onClose} className="cancelButton">Cancelar</button>
        </div>
        {errorMessage && (
                <div className="errorMessage">
                    {errorMessage}
                </div>
        )}
      </div>
    </div>
  );
};

export default AdressModal;
