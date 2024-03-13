import styles from "./index.module.css";

function ContainerList({ containers, page }) {

    const indexOfLastItem = page * 5;
    const indexOfFirstItem = indexOfLastItem - 5;
    const currentItems = containers.slice(indexOfFirstItem, indexOfLastItem);

    const orderArray = currentItems.map(order =>
        <li key={order.id} data-cy={'id'+order.id} className={styles.orderItem}>
            <div className={styles.interno}>
                <img src={order.img} className={styles.image} />
                <div className={styles.info}>
                    <p>{order.name}</p>
                    <p>Preço: R${order.price}</p>
                    <p>Status: {order._status}</p>
                </div>
            </div>
        </li>
    )
    return (
    <div className={styles.container}>
        <ul>{orderArray}</ul>
    </div>
  );
}

export default ContainerList;
