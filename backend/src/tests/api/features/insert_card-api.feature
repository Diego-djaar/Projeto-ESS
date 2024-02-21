Feature: Payment Methods API 

Scenario: Cadastrar cartão de crédito válido
    Given o cartao de nome "MasterCard", numero "4916123456789012", cvv "375", cpf "111.111.111-11" e validade "2028-10-08" não está cadastrado 
    When uma requisição "POST" foi enviada para "inserting/cartao" com Cartao(nome_cartao "MasterCard", numero_cartao "4916123456789012", cvv "134", cpf "111.111.111-11" e validade "2028-08-18")
    And a requisição está correta
    And o campo de "numero_cartao" de requisição é validado
    And o campo de "cpf" de requisição é validado
    And o campo de "validade" de requisição é validado
    Then o status da resposta deve ser "201"
    And o JSON da resposta indica que o cadastro foi bem sucedido
    And o cartao de nome "MasterCard", numero "4916123456789012", cvv "375", cpf "111.111.111-11" e validade "2028-10-08" está cadastrado 

Scenario: Cadastrar cartão de crédito com cpf inválido
    Given o cartao de nome "MasterCard", numero "4916123456789012", cvv "375", cpf "111.111.111" e validade "2028-10-08" não está cadastrado 
    When uma requisição "POST" foi enviada para "inserting/cartao" com Cartao(nome_cartao "MasterCard", numero_cartao "4916123456789012", cvv "134", cpf "111.111.111" e validade "2028-08-18")
    And a requisição está correta
    And o campo de "numero_cartao" de requisição é validado
    And o campo de "cpf" de requisição é validado
    And o campo de "validade" de requisição é validado
    Then o status da resposta deve ser "400"
    And o JSON da resposta indica que o cadastro foi mal sucedido
    And o JSON da resposta indica que o campo CPF foi mal preenchido
    And o cartao de nome "MasterCard", numero "4916123456789012", cvv "375", cpf "111.111.111" e validade "2028-10-08" não está cadastrado 

Scenario: Atualizar o numero do cartao
    Given o cartao de nome "MasterCard", numero "4916123456789012", cvv "375", cpf "111.111.111-11" e validade "2028-10-08" está cadastrado 
    When uma requisição "PUT" foi enviada para "update/cartao/{id}" com CartaoUpdate(nome_cartao "Visa", numero_cartao "5410 9876 5432 1098", cvv "937" e validade "2027-08-20")
    And a requisição está correta 
    And o campo de "numero_cartao" de requisição é validado
    And o campo de "cpf" de requisição é validado
    And o campo de "validade" de requisição é validado
    Then o status da resposta deve ser "200"
    And o JSON da resposta indica que a atualização foi bem sucedido
    And o cartao de nome "Visa", numero_cartao "5410 9876 5432 1098", cvv "937" e validade "2027-08-20" está cadastrado





    


