Feature: Calcular tempo estimado de entrega
As a usuário comum do sistema
I want to conferir o tempo estimado de entrega
So that eu possa saber em até quanto tempo receberei meu pedido

Cenário: Tempo estimado de entrega de pedido à caminho
Given o usuário de email “usuario@gmail.com” está na página “histórico de pedidos”
And o usuário de email “usuario@gmail.com” vê o pedido de número “80” no “histórico de pedidos” como “a caminho”
When o usuário de email “usuario@gmail.com” seleciona em “acompanhar pedido” de número “80”
Then o usuário de email “usuario@gmail.com” é enviado à pagina de “acompanhamento de pedido”
And o o usuário de email “usuario@gmail.com” pode ver o “tempo estimado de entrega”


Cenário: Tempo estimado de entrega de pedido cancelado
Given o usuário de email “usuario@gmail.com” está na página “histórico de pedidos”
And o usuário de email “usuario@gmail.com” vê o pedido de número “75” no “histórico de pedidos” como “cancelado”
When o usuário de email “usuario@gmail.com” seleciona em “acompanhar pedido” de número “75”
Then o usuário de email “usuario@gmail.com” é enviado à pagina de “acompanhamento de pedido”
And o o usuário de email “usuario@gmail.com” pode ver o aviso “pedido cancelado”

Cenário: Tempo estimado de entrega de pedido entregue
Given o usuário de email “usuario@gmail.com” está na página “histórico de pedidos”
And o usuário de email “usuario@gmail.com” vê o pedido de número “70” no “histórico de pedidos” como “cancelado”
When o usuário de email “usuario@gmail.com” seleciona em “acompanhar pedido” de número “70”
Then o usuário de email “usuario@gmail.com” é enviado à pagina de “acompanhamento de pedido”
And o o usuário de email “usuario@gmail.com” pode ver o aviso “pedido já foi entregue”
