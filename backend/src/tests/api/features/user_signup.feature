Feature: User Signup

    Scenario: Processar dados cadastrais bem sucedido
    Given Usuário "Enzo" não está cadastrado
    When uma requisição "POST" for enviada para "register", com Dados Cadastrais(nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: 010.010.010-23, endereço:  "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456")
    And a requisição está correta
    Then o campo "CPF" da requisição é validado
    And o campo "Data_de_nascimento" da requisição é validado
    And o campo "Email" da requisição é validado
    Then o status da resposta deve ser "200"
    And o JSON da resposta indica que o cadastro foi bem sucedido
    And Usuário "Enzo" está cadastrado

    Scenario: Processar dados cadastrais mal sucedido
    Given Usuário "Enzo" não está cadastrado
    When uma requisição "POST" for enviada para "register", com Dados Cadastrais(nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: "00.00.00", endereço:  "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456")
    Then o campo "CPF" da requisição é rejeitado
    And o status da resposta deve ser "400"
    And o JSON da resposta indica que o cadastro foi mal sucedido
    And o JSON da resposta indica que o campo "CPF" foi mal preenchido
    