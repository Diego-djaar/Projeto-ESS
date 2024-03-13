import styles from "./index.module.css";

import { useNavigate } from 'react-router-dom';

const ReturnButton = ({path}) => {
  const navigate = useNavigate();

  const handleVoltar = () => {
    navigate(path);
  };

  return (
    <div className={styles.returnButton}>
      <button onClick={handleVoltar} className={styles.returnButton}>
      Voltar
    </button>
    </div>
  );
};

export default ReturnButton;
