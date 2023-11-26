Feature: Carrinho de compras
As a usuário comum do sistema
I want to gerenciar os meus interesses de compra
So that eu consiga decidir o que comprar

Scenario: Remover item do carrinho com sucesso
Given eu estou logado com o email “usuario@gmail.com”
And estou na página “Carrinho”
And vejo o item “Camisa” com preço “60” na lista de itens do carrinho
And vejo o item “Calça” com preço “100” na lista de itens do carrinho
And vejo o preço “160” no carrinho
When eu removo “Camisa”
Then eu não vejo mais o item “Camisa” no carrinho
And eu vejo o item “Calça” com preço “100” no carrinho
And vejo uma mensagem de confirmação
And vejo que o preço agora é “100”

Scenario: Atualizar a quantidade de um item no carrinho
Given eu estou logado com o email “usuario@gmail.com”
And eu estou na página “Carrinho”
And eu vejo que  tem “2” do item “Camisa”
And o preço do carrinho é de “120”
When eu seleciono a opção “remover” para “Camisa”
Then eu ainda estou na página “Carrinho”
And eu vejo o número “1” ao lado do item “Camisa”
And o preço no carrinho é “60”

Scenario: Finalizar compra
Given eu estou logado com o email “usuario@gmail.com”
And estou na página “Carrinho”
And eu vejo “Camisa” na lista de itens do carrinho
When eu seleciono a opção “Realizar pagamento”
And eu efetuo o pagamento
Then eu recebo uma mensagem de confirmação
And eu estou na página “Carrinho”
And “Camisa” não está mais no carrinho

Scenario: Adicionar item no carrinho com sucesso
Given eu estou logado com o email “usuario@gmail.com”
And estou na página “Produto” de um item “Camisa”
And o carrinho tem “1” produto
When eu seleciono “Adicionar produto no carrinho”
Then eu recebo uma mensagem de confirmação
And eu vejo que o carrinho tem “2” itens no carrinho