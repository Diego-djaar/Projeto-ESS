Feature: Histórico de pedidos
As a usuário do sistema
I want to ver meu histórico de pedidos feitos
So that consigo verificar detalhes desses

Cenário: Exibir histórico de pedidos | Detalhes do pedido
Given cliquei na opção "Histórico de pedidos"
And estou numa tela com os "5" pedidos que fiz
When clico em "Detalhes do pedido" no pedido "Bolsa da Nike"
Then sou redirecionado para outra tela
And consigo ver os detalhes "Data 20/11/2023, Valor R$131,50, Status em entrega"

Cenário: Exibir histórico de pedidos | Paginação
Given cliquei na opção "Histórico de pedidos"
And estou numa tela com os "5" pedidos que fiz
When clico em "Próximo" no rodapé da página
Then os pedidos são atualizados
And consigo ver os "5" pedidos diferentes

Cenário: Exibir histórico de pedidos | Filtro por data
Given cliquei na opção "Histórico de pedidos"
And estou numa tela com os "5" pedidos que fiz
When clico em "Filtro por data" no menu de cima e seleciono "Últimos 5 meses"
Then os pedidos são atualizados
And consigo ver os "2" pedidos  que fiz nos "Últimos 5 meses" 

Cenário: Exibir histórico de pedidos | Filtro por fornecedor
Given cliquei na opção "Histórico de pedidos"
And estou numa tela com os "5" pedidos que fiz
When clico em "Filtro por fornecedor" no menu de cima e seleciono "Americanas"
Then os pedidos são atualizados
And consigo ver os "1" pedidos  que fiz com o fornecedor "Americanas" 

Feature: Exibir histórico de pedidos | Filtro por preço
Given cliquei na opção "Histórico de pedidos"
And estou numa tela com os "5" pedidos que fiz
When clico em "Filtro por preço" no menu de cima e seleciono "Maior que R$50,00"
Then os pedidos são atualizados
And consigo ver os "1" pedidos  que fiz com o preço "Maior que R$50,00" 