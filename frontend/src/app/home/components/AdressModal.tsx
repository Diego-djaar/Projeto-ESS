import styles from './AdressModal.module.css'; // Assuma que este é o seu arquivo de estilos para o modal

const AdressModal = ({ endereco, setEndereco, onSubmit, onClose, errorMessage }) => {

  const handleChange = (event) => {
    const { name, value } = event.target;
    setEndereco(prevEndereco => ({
      ...prevEndereco,
      [name]: name === 'numero' ? Number(value) : value
    }));
  };

  return (
    <div className={styles.modalBackground}>
      <div className={styles.modalContainer}>
        <div className={styles.modalHeader}>
          <h2>Editar Endereço</h2>
          <button onClick={onClose} className={styles.closeButton}>&times;</button>
        </div>
        <div className={styles.modalContent}>
          <input name="rua" value={endereco.rua} onChange={handleChange} placeholder="Rua *" />
          <input name="numero" type="number" value={endereco.numero} onChange={handleChange} placeholder="Número *" />
          <input name="bairro" value={endereco.bairro} onChange={handleChange} placeholder="Bairro *" />
          <input name="cidade" value={endereco.cidade} onChange={handleChange} placeholder="Cidade *" />
          <input name="estado" value={endereco.estado} onChange={handleChange} placeholder="Estado *" />
          <input name="cep" value={endereco.cep} onChange={handleChange} placeholder="CEP *" />
          <input name="pais" value={endereco.pais} onChange={handleChange} placeholder="País *" />
          <input name="complemento" value={endereco.complemento || ''} onChange={handleChange} placeholder="Complemento" />
        </div>
        <div className={styles.modalActions}>
          <button onClick={onSubmit} className={styles.saveButton}>Salvar Endereço</button>
          <button onClick={onClose} className={styles.cancelButton}>Cancelar</button>
        </div>
        {errorMessage && (
                <div className={styles.errorMessage}>
                    {errorMessage}
                </div>
        )}
      </div>
    </div>
  );
};

export default AdressModal;
