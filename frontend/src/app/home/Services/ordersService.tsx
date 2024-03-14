import axios from "axios";

async function allOrders ({setOrders, cpf}) {
    const response = await axios.get(`http://127.0.0.1:8000/backend/api/Orders/orders_by_user/`+cpf);
    setOrders(response.data.data);
}


async function filteredOrders ({setOrders, dict}) {
    const filteredDict = {};
    for (const key in dict) {
        if (dict.hasOwnProperty(key)) {
            filteredDict[key] = dict[key] === '' ? null : dict[key];
        }
    }
    const response = await axios.post(`http://127.0.0.1:8000/backend/api/Orders/orders_filtered`, filteredDict);
    setOrders(response.data.data);
}



export {allOrders, filteredOrders};