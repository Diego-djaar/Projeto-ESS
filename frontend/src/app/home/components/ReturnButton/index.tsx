// BotaoVoltar.jsx
import { useNavigate } from 'react-router-dom';

const ReturnButton = ({path}) => {
  const navigate = useNavigate();

  const handleVoltar = () => {
    navigate(path)
  };

  return (
    <button onClick={handleVoltar}>
      Voltar
    </button>
  );
};

export default ReturnButton;
