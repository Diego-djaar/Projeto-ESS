Feature: Carrinho API

Scenario: Obter carrinho por CPF
    Given o Carrinho_service retorna um carrinho com cpf "123.456.789-10"
    When uma requisição GET for enviada para "/backend/api/carrinho/view/123.456.789-10"
    Then o status da resposta deve ser "200"
    And o resultado do JSON deve ser "{"Itens:": {}, "Total": "0.00", "Endereço": "Endereço não registrado"}"

Scenario: Adicionar um produto válido ao carrinho
    Given um produto com ID "12345678" está disponível
    And o carrinho do cliente com CPF "123.456.789-10" está vazio
    When o cliente adiciona o produto com ID "12345678" ao carrinho
    Then o status da resposta deve ser "200"
    And o item deve estar no carrinho

Scenario: Remover um produto de um carrinho
    Given um produto com ID "12345678" está no carrinho de CPF "123.456.789-10"!
    When o cliente tenta remover o produto com ID "12345678" do carrinho
    Then o status da resposta deve ser "200"
    And o carrinho de CPF "123.456.789-10" está vazio

Scenario: Falha em remover um produto de um carrinho vazio
    Given o carrinho do cliente com CPF "123.456.789-10" está vazio
    When o cliente tenta remover o produto com ID "12345678" do carrinho
    Then o status da resposta deve ser "404"

Scenario: Limpar conteúdo do carrinho
    Given os produtos com ID "12345678" e "11111111" estão no carrinho de CPF "123.456.789-10"
    When o carrinho de CPF "123.456.789-10" é limpo
    Then o status da resposta deve ser "200"
    And o carrinho de CPF "123.456.789-10" está vazio

Scenario: Limpar a base de dados de carrinhos
    Given os carrinhos de CPF "123.456.789-10", "111.111.111-11" e "222.222.222-22" estão registrados
    When a base de dados de carrinhos é limpa
    Then o status da resposta deve ser "200"
    And a base de dados de carrinhos deve estar vazia

Scenario: Incrementar quantidade de um item no carrinho
    Given um produto com ID "12345678" de preço "29.99" está no carrinho de CPF "123.456.789-10" com quantidade "1"
    When o item é incrementado
    Then o status da resposta deve ser "200"
    And o produto de ID "12345678" no carrinho "123.456.789-10" deve ter a quantidade "2"
    And o total do carrinho de CPF "123.456.789-10" é "59.98"

Scenario: Decrementar quantidade de um item no carrinho com quantidade maior que 1
    Given um produto com ID "12345678" de preço "29.99" está no carrinho de CPF "123.456.789-10" com quantidade "2"
    When o item é decrementado
    Then o status da resposta deve ser "200"
    And o produto de ID "12345678" no carrinho "123.456.789-10" deve ter a quantidade "1"
    And o total do carrinho de CPF "123.456.789-10" é "29.99"

Scenario: Decrementar quantidade de um item no carrinho com quantidade 1
    Given um produto com ID "12345678" de preço "29.99" está no carrinho de CPF "123.456.789-10" com quantidade "1"
    When o item é decrementado
    Then o status da resposta deve ser "200"
    And o carrinho de CPF "123.456.789-10" está vazio

Scenario: Alterar endereço de destino do pedido
    Given o endereço do carrinho de CPF "123.456.789-10" não foi registrado
    When o endereço do carrinho de CPF "123.456.789-10" é alterado para "Rua , 225, Bairro, Cidade, Estado, CEP, País, Complemento"
    Then o carrinho de CPF "123.456.789-10" tem "Rua , 225, Complemento\nBairro, Cidade - Estado\nCEP: CEP\nPaís" no campo endereço
