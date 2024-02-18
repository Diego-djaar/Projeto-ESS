Feature: Carrinho API

Scenario: Obter carrinho por CPF
    Given o Carrinho_service retorna um carrinho com cpf "123.456.789-10"
    When uma requisição GET for enviada para "/carrinho/view/123.456.789-10"
    Then o status da resposta deve ser "200"
    And o resultado do JSON deve ser "{"Itens:": {}, "Total": "0.00", "Endereço": "Endereço não registrado"}"