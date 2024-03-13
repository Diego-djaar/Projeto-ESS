import styles from "./index.module.css";
import { useContext, useEffect, useState } from "react";
import { filteredOrders } from "../../Services/ordersService";

function FilterForm({cpf, setOrders}) {

    const [formData, setFormData] = useState({
        cpf: cpf,
        id: '',
        supplier_name: '',
        name: '',
        quantity: '',
        price_min: '',
        price_max: '',
        start_date: '',
        end_date: ''
    });

    const handleClear = () => {
        setFormData({
            cpf: cpf,
            id: '',
            supplier_name: '',
            name: '',
            quantity: '',
            price_min: '',
            price_max: '',
            start_date: '',
            end_date: ''
        });
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        filteredOrders({setOrders, dict:formData});
    };

    return (
        <form className={styles.form}>
            <div className={styles.formRow}>
                <input type="number" name="id" value={formData.id} placeholder="ID" onChange={handleChange} />
                <input type="text" name="supplier_name" value={formData.supplier_name} placeholder="Fornecedor" onChange={handleChange} />
                <input type="text" name="name" value={formData.name} placeholder="Nome do Produto" onChange={handleChange} />
                <input type="number" name="quantity" value={formData.quantity} placeholder="Quantidade" onChange={handleChange} />
            </div>
            <div className={styles.formRow}>
                <input type="text" name="price_min" value={formData.price_min} data-cy = "Preço Mínimo" placeholder="Preço Mínimo" onChange={handleChange} />
                <input type="text" name="price_max" value={formData.price_max} placeholder="Preço Máximo" onChange={handleChange} />
                <input type="date" name="start_date" value={formData.start_date} placeholder="Data Início" onChange={handleChange} />
                <input type="date" name="end_date" value={formData.end_date} placeholder="Data Fim" onChange={handleChange} />
            </div>
            <div className={styles.buttonRow}>
                <button className={styles.searchButton} type="submit" onClick={handleSubmit} data-cy="pesquisar">PESQUISAR</button>
                <button className={styles.clearButton} type="button" onClick={handleClear} data-cy="limpar">LIMPAR</button>
            </div>
        </form>
    );
}

export default FilterForm;