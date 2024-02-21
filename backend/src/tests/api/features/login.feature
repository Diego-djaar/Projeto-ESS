Feature: User Login

    Scenario: processar dados de login
    Given Usuário "Gabriel" está cadastrado
    And Usuário "Gabriel" possui senha "senha1234"
    When uma requisição "POST" for enviada para "login", com Dados Login(usuário: "Gabriel", senha: "senha1234")
    Then o status da resposta deve ser "200"
    And o campo "data" possui o campo "token" com valor $token_valor
    When uma requisição "POST" for enviada para "verify", com $token_valor
    Then o status da resposta deve ser "200"
    And o campo "data" possui o campo "user"
    And os elementos de "user" correspondem aos dados do usuário "Gabriel"

    Scenario: processar dados de login com usuário inexistente
    Given Usuário "Enzo" não está cadastrado
    When uma requisição "POST" for enviada para "login", com Dados Login(usuário: "Enzo", senha: "senha1234")
    Then o status da resposta deve ser "401"
    And o campo "message" tem o valor "CPF ou Senha incorretos"

    Scenario: processar dados de login com senha incorreta
    Given Usuário "Gabriel" está cadastrado
    And Usuário "Gabriel" possui senha "senha1234"
    When uma requisição "POST" for enviada para "login", com Dados Login(usuário: "Gabriel", senha: "senha1235")
    Then o status da resposta deve ser "401"
    And o campo "message" tem o valor "CPF ou Senha incorretos"
