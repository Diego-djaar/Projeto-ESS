Feature: Cancelamento de pedidos
As a usuário comum do sistema 
I want to acessar meus pedidos 
So that eu possa cancelar meus pedidos 

Cenário: Cancelamento de pedido bem sucedido
Given o usuário de email “usuario@gmail.com” 
And o usuário vê o pedido de número “59” no “histórico de pedidos”
When o usuário seleciona em "detalhes do pedido" do pedido de número "59"
Then ele consegue ver os detalhes data do pedido "20/11/2023", valor "R$131,50" e status "a caminho"
When o usuário seleciona em “cancelar pedido” 
Then o usuário recebe “requisição do motivo de cancelamento” 
And o usuário preenche com o motivo de cancelamento com “Pedido demorou muito”
Then o usuário recebe a mensagem "Pedido cancelado com sucesso!"
And o pedido de número “59” está no “histórico de pedidos” como “cancelado”
 
Cenário: Cancelamento de pedido sem o preenchimento de informações
Given o usuário de email “usuario@gmail.com” 
And o usuário vê o pedido de número “59” no “histórico de pedidos”
When o usuário seleciona em "detalhes do pedido" do pedido de número "59"
Then ele consegue ver os detalhes data do pedido "20/11/2023", valor "R$131,50" e status "a caminho"
And o usuário seleciona em “cancelar pedido” 
Then o usuário recebe “requisição do motivo de cancelamento”
And o usuário seleciona em “confirmar o cancelamento”
Then o usuário recebe a mensagem “Você precisa preencher todos os dados, tente novamente!”
And o usuário recebe “requisição de senha e motivo de cancelamento” novamente

Cenário: Cancelamento de pedido já entregue
Given o usuário de email “usuario@gmail.com” 
And o usuário vê o pedido de número “59” no “histórico de pedidos”
When o usuário seleciona em "detalhes do pedido" do pedido de número "59"
Then ele consegue ver os detalhes data do pedido "20/11/2023", valor "R$131,50" e status "entregue" 
When o usuário seleciona em “cancelar pedido” 
Then o usuário recebe “requisição do motivo de cancelamento” 
And o usuário preenche com o motivo de cancelamento com “Não posso mais receber o produto”
Then o usuário recebe a mensagem "Este pedido já foi entregue"
And o usuário volta para "detalhes do pedido"

Cenário: Cancelamento de pedido já cancelado
Given o usuário de email “usuario@gmail.com” 
And o usuário vê o pedido de número “59” no “histórico de pedidos”
When o usuário seleciona em "detalhes do pedido" do pedido de número "59"
Then ele consegue ver os detalhes data do pedido "20/11/2023", valor "R$131,50" e status "cancelado"
And o usuário seleciona em “cancelar pedido” 
Then o usuário recebe “requisição do motivo de cancelamento” 
And o usuário preenche com o motivo de cancelamento com “Não quero mais o produto”
Then o usuário recebe a mensagem "Este pedido já foi cancelado"
And o usuário volta para "detalhes do pedido"

Cenário: Vendo lista de pedidos cancelados
Given o usuário de email "usuario@gmail.com" está na página "histórico de pedidos"
And o usuário vê os pedidos "10", "12", "15" e "19" 
When o usuário clica em "pedidos cancelados"
Then o usuário agora está na página "pedidos cancelados" e vê os pedidos "12" e "15"