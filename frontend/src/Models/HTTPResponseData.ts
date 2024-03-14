import ItemData from "./ItemData"

export default interface HTTPResponseData {
    message: string;
    status_code: number;
    data: CartData | null;
}

interface CartData {
    Itens: ItemData[];
    Total: number;
    Endereço: string;
}