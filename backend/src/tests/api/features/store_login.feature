Feature: Login de Lojas

    Scenario: Login de loja já cadastrada
    Given Loja "Hortifruti", de CNPJ "37.565.457/0001-90" já está cadastrada com senha "htft8"
    When Uma requisição POST for enviada para "login", com as seguintes informações (CNPJ: "37.565.457/0001-90", Senha: "htft8")
    Then O status da resposta deve ser "200"
    And O campo "message" tem o resultado positivo "Login com sucesso"

    Scenario: Login de loja não cadastrada
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" não está cadastrada
    When Uma requisição POST for enviada para "login", com as seguintes informações (CNPJ: "48.449.992/0001-65", Senha: "htft8")
    Then O status da resposta deve ser "400"
    And O campo "message" tem o resultado "Login falhou, essa loja não deve estar cadastrada"

    Scenario: Tentativa de Login com senha incorreta
    Given Loja "Hortifruti", de CNPJ "37.565.457/0001-90" já está cadastrada com senha "htft8"
    When Uma requisição POST for enviada para "login", com as seguintes informações (CNPJ: "37.565.457/0001-90", Senha: "bananinha")
    Then O status da resposta deve ser "401"
    And O campo "message" tem o resultado negativo "CNPJ ou Senha incorretos"
