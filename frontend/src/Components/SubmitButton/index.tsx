import styles from "./index.module.css";


const SubmitButton = ({onClick, value, Datacy}) => {

    return (
        <>  
        <button data-cy = {Datacy} className={styles.submissionButton} onClick = {onClick}>{value}</button>   
        </>
    )

}

export default SubmitButton; 