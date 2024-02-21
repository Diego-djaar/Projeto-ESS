Feature: Manutenção de lojas cadastradas

    Scenario: Recuperação de senha
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" já está cadastrada com senha "htft8"
    When Uma requisição POST for enviada para "login/retrieve_password", com as seguintes informações (CNPJ: "48.449.992/0001-65", Email: "Hortifruti@loja.com", Nova_senha: "1234")
    Then o status da resposta deve ser "200"
    And A senha da loja "Hortifruti" agora é "1234"
    And O campo "message" tem valor "Atualização de dados bem sucedida"

    Scenario: Recuperação de senha com dados incorretos
    Given Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" já está cadastrada com senha "htft8"
    When Uma requisição POST for enviada para "login/retrieve_password", com as seguintes informações (CNPJ: "BrenoMiranda", Email: "Hortifruti@loja.com", Nova_senha: "1234")
    Then O status da resposta deve ser "401"
    And O campo "message" tem valor "CNPJ ou Email incorretos"

    Scenario: Modificação de dados de uma loja
    Given Loja "Hortifruti", de CNPJ "48.449.992/0001-65" já está cadastrada com senha "htft8"
    And Um administrador da loja está logado
    When Uma requisição POST for enviada para "store_signup", com as seguintes informações (CNPJ: "48.449.992/0001-65", Senha: "htft8", novoNome: "Hortifrutaria", novaCategoria: "Eletronicos")
    Then O status da resposta deve ser "200"
    And O nome da loja é atualizado para "Hortifrutaria"
    And A categoria da loja é atualizada para "Eletronicos"
    And O campo "message" tem o valor "Atualização de dados bem sucedida"
    