import styles from "./index.module.css";

const Button = ({value, onClick}) => {

    return <button className={styles.buttom} onClick={onClick}>{value} </button>

}

export default Button