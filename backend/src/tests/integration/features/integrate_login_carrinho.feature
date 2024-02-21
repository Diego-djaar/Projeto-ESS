Feature: Integrar User Login e Carrinho

    Scenario: Logar e usar carrinho
    Given Usuário "Gabriel" está cadastrado
    And um produto com ID "99999999" está no carrinho de "Gabriel"
    And Usuário "Gabriel" possui senha "senha1234"
    When uma requisição "POST" for enviada para "login", com Dados Login(usuário: "Gabriel", senha: "senha1234")
    Then o status da resposta deve ser "200"
    And o campo "data" possui o campo "token" com valor $token_valor
    When uma requisição "POST" for enviada para "verify", com $token_valor
    Then o status da resposta deve ser "200"
    When o cliente tenta remover o produto com ID "99999999" do carrinho de "Gabriel"
    Then o status da resposta deve ser "200"
    And o carrinho de "Gabriel" está vazio