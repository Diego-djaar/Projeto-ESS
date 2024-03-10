import AdressData from '../models/AdressData'
import { useCpf } from '../context/HomeContext/CpfContext';
import { useState } from 'react';
import AdressModal from './AdressModal';
import axios from 'axios';
import styles from './AdressComponent.module.css'
import { useEffect } from 'react';

interface AdressProps {
  endereco_atual: string
}

const AdressComponent: React.FC<AdressProps> = ({ endereco_atual } ) => {
    const [mostrarModal, setMostrarModal] = useState(false);
    const [showConfirmation, setShowConfirmation] = useState(false);
    const [endereco_visivel, setEnderecoVisivel] = useState(endereco_atual)

    function formatarEndereco(endereco: AdressData): string {
      let enderecoCompleto = `${endereco.rua}, ${endereco.numero}`;
      if (endereco.complemento) {
        enderecoCompleto += `, ${endereco.complemento}`;
      }
      enderecoCompleto += `\n${endereco.bairro}, ${endereco.cidade} - ${endereco.estado}\nCEP: ${endereco.cep}\n${endereco.pais}`;
      return enderecoCompleto;
    }
    

    // Função para mostrar o pop-up de confirmação por um tempo limitado
    const showConfirmationPopup = () => {
        setShowConfirmation(true);
        setTimeout(() => {
            setShowConfirmation(false);
        }, 3000); // O pop-up será escondido após 3 segundos
    };

    useEffect(() => {
      console.log('Show Confirmation changed: ', showConfirmation);
    }, [showConfirmation]);
  

    const [endereco, setEndereco] = useState<AdressData>({
      rua: '',
      numero: 0,
      bairro: '',
      cidade: '',
      estado: '',
      cep: '',
      pais: '',
      complemento: ''
    });
    const [ cpf ] = useCpf(); // Supondo que você tenha o CPF do usuário
    const [formError, setFormError] = useState('');
  
    const handleOpenModal = () => {
      setMostrarModal(true);
      setFormError('')
    };
  
    const handleCloseModal = () => {
      setMostrarModal(false);
      setFormError('');
    };
  
    const handleSubmit = async () => {
        // Verifique se todos os campos necessários estão preenchidos
        if (
          !endereco.rua || 
          !endereco.numero ||
          !endereco.bairro ||
          !endereco.cidade ||
          !endereco.estado ||
          !endereco.cep ||
          !endereco.pais
          // Complemento é opcional, por isso não está listado aqui
        ) {
          console.error('Por favor, preencha todos os campos obrigatórios.');
          setFormError('Por favor, preencha todos os campos obrigatórios.');
          return; // Não prosseguir com a submissão se a validação falhar
        } else {
            setFormError('');
        }
    
        try {
            const response = await axios.put(
              `http://127.0.0.1:8000/backend/api/carrinho/alterar_endere%C3%A7o?CPF=${cpf}`, 
              endereco
            );
          
            if (response.status === 200) {
                console.log('Endereço alterado com sucesso');
                handleCloseModal();
                showConfirmationPopup(); // Mostra o pop-up de confirmação
                setEnderecoVisivel(formatarEndereco(endereco))
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
            console.error(errorMessage);
        }
    };
    
  
    return (
      <>
        <p className={styles.addressInfo}>Endereço: {endereco_visivel}</p>
        <button className={styles.modelButton} onClick={handleOpenModal}>Alterar Endereço</button>
        {mostrarModal && (
          <AdressModal
          endereco={endereco}
          setEndereco={setEndereco}
          onSubmit={handleSubmit}
          onClose={handleCloseModal}
          errorMessage={formError}
          />
        )}
        {showConfirmation && (
        <div className={styles.confirmationPopup}>
            Endereço alterado com sucesso!
        </div>
      )}
      </>
    );
  };
  
  export default AdressComponent;