Feature: Inserir pix API 

Scenario: Cadastrar pix válido
    Given o pix de cpf "111.111.111-11" e nome "Breno Gabriel de Melo Lima" não está cadastrado na base de dados
    When uma requisição "POST" for enviada para "inserir/pix", com Pix(nome "Breno Gabriel de Melo Lima", cpf "111.111.111-11")
    And a requisição está correta
    Then o campo "CPF" da requisição é validado
    And o status da resposta deve ser "201"
    And o JSON da resposta indica que o cadastro foi bem sucedido 
    And o pix de cpf "111.111.111-11" e nome "Breno Gabriel de Melo Lima" está cadastrado na base de dados

Scenario: Cadastrar pix com cpf inválido
    Given o pix de cpf "111.111.111" e nome "Breno Gabriel de Melo Lima" não está cadastrado na base de dados
    When uma requisição "POST" for enviada para "inserir/pix", com Pix(nome "Breno Gabriel de Melo Lima", cpf "111.111.111")
    And a requisição está correta
    Then o campo "CPF" da requisição é validado
    And o status da resposta deve ser "201"
    And o JSON de resposta indica que o cadastro foi mal sucedido 
    And o pix de cpf "111.111.111-11" e nome "Breno Gabriel de Melo Lima" não está cadastrado na base de dados


