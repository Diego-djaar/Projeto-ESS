Feature: Integrar Login e Cadastro de Usuário

    Scenario: Logar após Cadastrar
    Given Usuário "Enzo" não está cadastrado
    When uma requisição "POST" for enviada para "register", com Dados Cadastrais(nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: 010.010.010-23, endereço:  "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456")
    Then o status da resposta deve ser "200"
    And o JSON da resposta indica que o cadastro foi bem sucedido
    And Usuário "Enzo" está cadastrado
    When uma requisição "POST" for enviada para "login", com Dados Login(usuário: "Enzo", senha: "Xyzw3456")
    Then o status da resposta deve ser "200"
    And o campo "data" possui o campo "token" com valor "$token_valor"
    When uma requisição "POST" for enviada para "verify", com "$token_valor"
    Then o status da resposta deve ser "200"
    And o campo "data" possui o campo "user"
    And os elementos de "user" correspondem aos dados do usuário "Enzo"
    
    Scenario: Logar senha errada após Cadastrar
    Given Usuário "Enzo" não está cadastrado
    When uma requisição "POST" for enviada para "register", com Dados Cadastrais(nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: 010.010.010-23, endereço:  "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456")
    Then o status da resposta deve ser "200"
    And o JSON da resposta indica que o cadastro foi bem sucedido
    And Usuário "Enzo" está cadastrado
    When uma requisição "POST" for enviada para "login", com Dados Login(usuário: "Enzo", senha: "Xyzw3457")
    Then o status da resposta deve ser "401"