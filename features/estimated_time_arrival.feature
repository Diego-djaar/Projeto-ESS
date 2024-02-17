Feature: Calcular tempo estimado de entrega
As a usuário comum do sistema
I want to conferir o tempo estimado de entrega
So that eu possa saber em até quanto tempo receberei meu pedido

Cenário: Cálculo de tempo estimado de entrega com CEP do user inválido
Given o usuário de email "usuario@gmail.com" e CEP "11111111" está na página "tempo estimado de entrega" da loja "Enovo"
And o usuário seleciona "calcular estimativa de entrega" 
Then o usuário recebe a mensagem "Seu CEP é inválido, coloque nas suas informações de endereço um CEP válido"
And o usuário é redirecionado para a página de "alteração dos dados cadastrais"

Cenário: Cálculo de tempo estimado de entrega entre o mesmo estado
Given o usuário de email "usuario@gmail.com" e CEP "55875970" está na página "tempo estimado de entrega" da loja "HD"
And o usuário seleciona "calcular estimativa de entrega" 
Then o usuário pode ver a data de estimativa de entrega do produto "16/02/2024"
And o modelo de entrega "tradicional"

Cenário: Cálculo de tempo estimado de entrega na mesma região
Given o usuário de email "usuario@gmail.com" e CEP "58819-970" está na página "tempo estimado de entrega" da loja "Jpro"
And o usuário seleciona "calcular estimativa de entrega" 
Then o usuário pode ver a estimativa de entrega do produto "18/02/2024" 
And o modelo de entrega "expresso"

Cenário: Cálculo de tempo estimado de entrega entre regiões diferentes
Given o usuário de email "usuario@gmail.com" e CEP "01153-000" está na página "tempo estimado de entrega" da loja "Kogitech"
And o usuário seleciona "calcular estimativa de entrega" 
Then o usuário pode ver a estimativa de entrega do produto "28/02/2024" 
And o modelo de entrega "aéreo"

Cenário: Consulta de tempo estimado de entrega de pedido
Given o usuário de email “usuario@gmail.com” e CEP "58819-970" está na página “histórico de pedidos”
And o usuário vê o pedido de número “80” no “histórico de pedidos” 
When o usuário seleciona em "detalhes do pedido" do pedido de número "80"
Then ele consegue ver os detalhes data do pedido "20/11/2023", valor "R$131,50", status "a caminho", data estimada de entrega "15/02/2024" e o modelo de entrega "expresso"
