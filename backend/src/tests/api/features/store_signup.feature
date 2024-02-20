Feature: Cadastro de Lojas

    Scenario: Cadastro bem sucedido
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" não está cadastrada
    When Uma requisição POST for enviada para "stores/store_signup", com as seguintes informações (Nome: "Hortifruti", CNPJ: "48.449.992/0001-65", Email: "Hortifruti@loja.com", Senha: "htft8", Categoria: "Alimenticio")
    Then o status da resposta deve ser "200"
    And o campo "message" tem o valor "Loja cadastrada com sucesso"

    Scenario: Tentativa de cadastro de loja já cadastrada
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" já está cadastrada
    When Uma requisição POST for enviada para "stores/store_signup" com as seguintes informações (Nome: "Hortifruti", CNPJ: "48.449.992/0001-65", Email: "Hortifruti@loja.com", Senha: "htft8", Categoria: "Alimenticio")
    Then o status da resposta deve ser "401"
    And o campo "message" tem o valor "Já existe uma loja registrada com esses dados"

    Scenario: Tentativa de cadastro com dados em formato invalido
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" não está cadastrada
    When Uma requisição POST for enviada para "stores/store_signup", com as seguintes informações (Nome: "Hortifruti", CNPJ: "Mengão_da_massa", Email: "Hortifruti@loja.com", Senha: "htft8", Categoria: "Alimenticio")
    Then o status da resposta de ser "400"
    And O campo "message" tem o valor "informações com formato invalido"
    