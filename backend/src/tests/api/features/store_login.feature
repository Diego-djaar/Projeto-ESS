Feature: Login de Lojas

    Scenario: Login de loja já cadastrada
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" já está cadastrada com senha "htft8"
    When Uma requisição POST for enviada para "stores/store_login", com as seguintes informações (CNPJ: "48.449.992/0001-65", Senha: "htft8")
    Then O status da resposta deve ser "200"
    And O campo "message" tem o valor "Login com sucesso"

    Scenario: Login de loja não cadastrada
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" não está cadastrada
    When Uma requisição POST for enviada para "stores/store_login", com as seguintes informações (CNPJ: "48.449.992/0001-65", Senha: "htft8")
    Then O status da resposta deve ser "400"
    And O campo "message" tem o valor "Login falhou, essa loja não deve estar cadastrada"

    Scenario: Tentativa de Login com senha incorreta
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" já está cadastrada com senha "htft8"
    When Uma requisição POST for enviada para "stores/store_login", com as seguintes informações (CNPJ: "48.449.992/0001-65", Senha: "bananinha")
    Then O status da resposta deve ser "401"
    And O campo "message" tem o valor "CNPJ ou Senha incorretos"
