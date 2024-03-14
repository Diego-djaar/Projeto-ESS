import styles from "./index.module.css";

const Button = ({value, onClick, DataCy}) => {

    return <button data-cy = {DataCy} className={styles.buttom} onClick={onClick}>{value} </button>

}

export default Button