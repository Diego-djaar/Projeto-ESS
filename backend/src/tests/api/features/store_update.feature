Feature: Manutenção de lojas cadastradas

    Scenario: Recuperação de senha
    Given Loja "Hortifruti", de CNPJ "121212" já está cadastrada com senha "htft8"
    When Uma requisição POST for enviada para "login/retrieve_password", com as seguintes informações (CNPJ: "121212", Email: "@loja.com", Nova_senha: "12345")
    Then o status da resposta deve ser "200"
    And A senha da loja de CNPJ "121212" agora é "12345"
    And O campo "message" tem o resultado positivo "Atualização de dados bem sucedida"



    Scenario: Recuperação de senha com dados incorretos
    Given Loja "Hortifruti", de CNPJ "121212" já está cadastrada com senha "htft8"
    When Uma requisição POST for enviada para "login/retrieve_password", com as seguintes informações (CNPJ: "BrenoMiranda", Email: "Hortifruti@loja.com", Nova_senha: "1234")
    Then O status da resposta deve ser "401"
    And o campo "message" tem o resultado negativo "CNPJ ou Email incorretos"

    Scenario: Modificação de dados de uma loja
    Given Loja "Hortifruti", de CNPJ "121212" já está cadastrada com senha "12345"
    When Uma requisição POST for enviada para "store/change_store_data", com as seguintes informações (CNPJ: "121212", Senha: "12345", novoNome: "Hortifrutaria", novaCategoria: "Eletronicos", novoEmail: "laland@loja")
    Then O status da resposta deve ser "200"
    And O nome da loja de CNPJ "121212" é atualizado para "Hortifrutaria"
    And A categoria da loja de CNPJ "121212" é atualizada para "Eletronicos"
    And O campo "message" tem o resultado "Atualização de dados bem sucedida"
    