Feature: Cancelamento de pedidos
As a usuário comum do sistema 
I want to acessar meus pedidos 
So that eu possa cancelar meus pedidos 

Cenário: Cancelamento de pedido bem sucedido
Given o usuário de email “usuario@gmail.com” está na página “histórico de pedidos”
And o usuário de email “usuario@gmail.com” vê o pedido de número “59” no “histórico de pedidos” como “a caminho”
When o usuário de email “usuario@gmail.com” seleciona em “cancelar pedido” do pedido de número “59”
Then o usuário de email “usuario@gmail.com” recebe “requisição de senha e motivo de cancelamento” 
And o usuário de email “usuario@gmail.com” preenche com o motivo de cancelamento com “Pedido demorou muito” e preenche sua senha corretamente
Then o pedido de número “59” está no “histórico de pedidos” como “cancelado”
And o usuário de email “usuario@gmail.com” recebe a mensagem “Pedido cancelado com sucesso!”
 
Cenário: Cancelamento de pedido com senha errada
Given o usuário de email “usuario@gmail.com” está na página “histórico de pedidos”
And o usuário de email “usuario@gmail.com” vê o pedido de número “59” no “histórico de pedidos” como “à caminho”
When o usuário de email “usuario@gmail.com” seleciona em “cancelar pedido” do pedido de número “59”
Then o usuário de email “usuario@gmail.com” recebe “requisição de senha e motivo de cancelamento”
And o usuário de email “usuario@gmail.com” preenche com o motivo de cancelamento com “Pedido demorou muito” e preenche a senha errada
Then o usuário de email “usuario@gmail.com” recebe a mensagem “Senha incorreta, tente novamente!”
And o usuário de email “usuario@gmail.com” recebe “requisição de senha e motivo de cancelamento” novamente

Cenário: Cancelamento de pedido sem o preenchimento de informações
Given o usuário de email “usuario@gmail.com” está na página “histórico de pedidos”
And o usuário de email “usuario@gmail.com” vê o pedido de número “59” no “histórico de pedidos” como “a caminho”
When o usuário de email “usuario@gmail.com” seleciona em “cancelar pedido” do pedido de número “59”
Then o usuário de email “usuario@gmail.com” recebe “requisição de senha e motivo de cancelamento”
And o usuário de email “usuario@gmail.com” seleciona em “confirmar o cancelamento”
Then o usuário de email “usuario@gmail.com” recebe a mensagem “Você precisa preencher todos os dados, tente novamente!”
And o usuário de email “usuario@gmail.com” recebe “requisição de senha e motivo de cancelamento” novamente