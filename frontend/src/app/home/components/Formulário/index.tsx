import styles from "./index.module.css";

const Formulario = ({ label }) => {
  return (
    <div className={styles.forms}>
      <label className={styles.label}>{label}</label>
      <input className = {styles.caixaTexto} type="text" />
    </div>
  );
};

export default Formulario;
