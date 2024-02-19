Feature: Carrinho API

Scenario: Obter carrinho por CPF
    Given o Carrinho_service retorna um carrinho com cpf "123.456.789-10"
    When uma requisição GET for enviada para "/carrinho/view/123.456.789-10"
    Then o status da resposta deve ser "200"
    And o resultado do JSON deve ser "{"Itens:": {}, "Total": "0.00", "Endereço": "Endereço não registrado"}"

Scenario: Adicionar um produto válido ao carrinho
    Given um produto com ID "12345678" está disponível
    And o carrinho do cliente com CPF "123.456.789-10" está vazio
    When o cliente adiciona o produto com ID "12345678" ao carrinho
    Then o status da resposta deve ser "200"
    And o item deve estar no carrinho