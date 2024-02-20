Feature: Cadastro de Lojas

    Scenario: Cadastro bem sucedido
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" não está cadastrada
    When Uma requisição POST for enviada para "signup", com as seguintes informações (Nome: "Hortifruti", CNPJ: "48.449.992/0001-65", Email: "Hortifruti@loja.com", Senha: "htft8", Categoria: "Alimenticio")
    Then o status da resposta deve ser "200"
    And o campo "message" tem o resultado positivo "Loja cadastrada com sucesso"

    Scenario: Tentativa de cadastro de loja já cadastrada
    Given Loja "Lojalegal", de CNPJ "36.565.457/0001-90" já está cadastrada
    When Uma requisição POST for enviada para "signup", com as seguintes informações (Nome: "Hortifruti", CNPJ: "36.565.457/0001-90", Email: "vitor@loja.com", Senha: "123", Categoria: "Alimento")
    Then O status da resposta deve ser "401"
    And O campo "message" tem o resultado negativo "Já existe uma loja registrada com esses dados"

    Scenario: Tentativa de cadastro com dados em formato invalido
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" não está cadastrada
    When Uma requisição POST for enviada para "signup", com as seguintes informações (Nome: "Hortifruti", CNPJ: "Mengão_da_massa", Email: "Hortifruti@loja.com", Senha: "htft8", Categoria: "Alimenticio")
    Then o status da resposta de ser "400"
    And O campo "message" tem o valor "informações com formato invalido"
    