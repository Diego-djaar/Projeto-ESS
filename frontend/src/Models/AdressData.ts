export default interface AdressData {
    rua: string;
    numero: number;
    bairro: string;
    cidade: string;
    estado: string;
    cep: string;
    pais: string;
    complemento?: string;
  }