import { useContext, useEffect, useState } from "react";
import styles from "./index.module.css";
import Pichu from "../../components/logo";
import ContainerList from "../../components/container_order";
import PaginationButtons from "../../components/paginationButton";
import FilterForm from "../../components/filterForm";
import * as OrdersService from "../../Services/ordersService";
import { useCpf } from '../../Context/CpfContext';

const OrdersHistory = () => {
  const [cpf] = useState(useCpf());
  const [orders, setOrders] = useState([]);
  const [page, setPage] = useState(1);
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, [page]);
  useEffect(() => {
    OrdersService.allOrders({setOrders, cpf});
  }, [cpf]);

  return (<section className={styles.container}>
    <div className={styles.titleContainer}>
      <div className={styles.imageContainer}><Pichu></Pichu></div>
      <h2 className={styles.title}>Pedidos</h2>
    </div>
    <FilterForm cpf={cpf} setOrders={setOrders}/>
    <ContainerList containers={orders} page={page}/>
    <PaginationButtons setPage={setPage} page={page} maxPage={Math.ceil(orders.length/5)}/>
    </section>
    
  );
};

export default OrdersHistory;