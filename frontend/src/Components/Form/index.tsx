import styles from "./index.module.css";

const Form = ({placeholder, onChange, Datacy}) => {

    return (
        <>
        <input data-cy = {Datacy} type="text" className={styles.caixaTexto} placeholder={placeholder}  onChange={onChange}/>
        </>
    )

}

export default Form;