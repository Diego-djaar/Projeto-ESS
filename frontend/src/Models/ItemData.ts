export default interface ItemData {
  id: string; // Acessos a database serão pelo ID (8 dígitos)
  nome: string; // Nome visível na interface
  description: string;
  price: string;
  quantidade: number;
  img: string | null; // Path para o arquivo
  }