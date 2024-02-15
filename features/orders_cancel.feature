Feature: Cancelamento de pedidos
As a usuário comum do sistema 
I want to acessar meus pedidos 
So that eu possa cancelar meus pedidos 

Cenário: Cancelamento de pedido bem sucedido
Given o usuário de email “usuario@gmail.com” e senha "password" está na página “histórico de pedidos”
And o usuário vê o pedido de número “59” no “histórico de pedidos” como “a caminho”
When o usuário seleciona em “cancelar pedido” do pedido de número “59”
Then o usuário recebe “requisição de senha e motivo de cancelamento” 
And o usuário preenche com o motivo de cancelamento com “Pedido demorou muito” e preenche sua senha "password" corretamente
Then o pedido de número “59” está no “histórico de pedidos” como “cancelado”
And o usuário recebe a mensagem “Pedido cancelado com sucesso!”
 
Cenário: Cancelamento de pedido com senha errada
Given o usuário de email “usuario@gmail.com” e senha "password" está na página “histórico de pedidos”
And o usuário vê o pedido de número “59” no “histórico de pedidos” como “à caminho”
When o usuário seleciona em “cancelar pedido” do pedido de número “59”
Then o usuário recebe “requisição de senha e motivo de cancelamento”
And o usuário preenche com o motivo de cancelamento com “Pedido demorou muito” e preenche a senha "wrongpassword"
Then o usuário recebe a mensagem “Senha incorreta, tente novamente!”
And o usuário recebe “requisição de senha e motivo de cancelamento” novamente

Cenário: Cancelamento de pedido sem o preenchimento de informações
Given o usuário de email “usuario@gmail.com” e senha "password" está na página “histórico de pedidos”
And o usuário vê o pedido de número “59” no “histórico de pedidos” como “a caminho”
When o usuário seleciona em “cancelar pedido” do pedido de número “59”
Then o usuário recebe “requisição de senha e motivo de cancelamento”
And o usuário seleciona em “confirmar o cancelamento”
Then o usuário recebe a mensagem “Você precisa preencher todos os dados, tente novamente!”
And o usuário recebe “requisição de senha e motivo de cancelamento” novamente
