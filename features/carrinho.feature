Feature: Carrinho de compras
As a usuário comum do sistema
I want to gerenciar os meus interesses de compra
So that eu possa tomar decisões informadas sobre o que comprar

Scenario: Remover item do carrinho com sucesso
Given eu estou logado com o email “usuario@gmail.com”
And estou na página “Carrinho”
And vejo o item “Camisa” com preço “60” e quantidade "1" na lista de itens do carrinho
And vejo o item “Calça” com preço “100” e quantidade "1" na lista de itens do carrinho
And vejo o preço “160” no carrinho
When eu removo “Camisa”
Then eu não vejo mais o item “Camisa” no carrinho
And eu vejo o item “Calça” com preço “100” e quantidade "1" no carrinho
And vejo uma mensagem de confirmação
And vejo que o preço total agora é “100”

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

Scenario: Falha no pagamento
Given eu estou logado com o email "usuario@gmail.com"
And eu estou na página "Pagamento"
When eu realizo o pagamento
Then eu vejo uma mensagem de erro
And nenhum dinheiro sai da minha conta
And Eu estou na página "Carrinho"
And o carrinho permanece inalterado

Scenario: Falha em remover item do carrinho
Given eu estou logado com o email “usuario@gmail.com”
And estou na página “Carrinho”
And vejo o item “Camisa” com preço “60” na lista de itens do carrinho
And vejo o item “Calça” com preço “100” na lista de itens do carrinho
And vejo o preço “160” no "Total" carrinho
When eu tento remover “Camisa”
Then eu recebo uma mensagem de erro
And eu ainda vejo o item "Camisa" com preço "60" na lista de itens do carrinho
And eu vejo o item “Calça” com preço “100” no carrinho
And vejo que o preço ainda é “160”

Scenario: Produto do carrinho esgotado
Given eu estou logado com o email "usuario@gmail.com"
And eu estou na página "Carrinho"
And vejo o item "Camisa" no carrinho
When eu tento realizar o pagamento
Then recebo uma mensagem avisando que o produto "Camisa" está fora de estoque
And estou na página "Carrinho"
And o produto "Camisa" está marcado como "Esgotado"

Scenario: Ir para o carrinho
Given estou logado com o email "usuario@gmail.com" 
And estou em qualquer página do sistema
When eu tento clicar no ícone do carrinho
Then eu estou na página "Carrinho"


