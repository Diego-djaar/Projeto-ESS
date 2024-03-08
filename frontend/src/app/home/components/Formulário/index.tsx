import styles from "./index.module.css";

const Formulario = ({ paymentType}) => {
  return (
    <div>
      <form className={styles.forms}>
      <label className={styles.label}>Nome completo</label>
      <input className = {styles.caixaTexto} type="text" placeholder="Digite aqui o seu nome completo"/>
      <label className={styles.label}>CPF</label>
      <input className = {styles.caixaTexto} type="text" placeholder="Digite aqui o seu CPF"/>
      <br />
      <input type="Submit" value={paymentType} className={styles.submissionButton}/>
    </form>
    </div>
  );
};

export default Formulario;
