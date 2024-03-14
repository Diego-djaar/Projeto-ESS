Scenario: Atualizar o numero do cartao
    Given o cartao de id "4574450647725381807" tipo "cartao", nome "MasterCard", numero "4916123456789012", cvv "375", cpf "111.111.111-11" e validade "2028-10-08" está cadastrado 
    When uma requisição "PUT" foi enviada para "update/cartao/{id}" com CartaoUpdate(nome_cartao "Visa", numero_cartao "5410987654321098", cvv "937" e validade "2027-08-20")
    And a requisição está correta 
    And o campo de "numero_cartao" de requisição é validado
    And o campo de "cpf" de requisição é validado
    And o campo de "validade" de requisição é validado
    Then o status da resposta deve ser "200"
    And o JSON da resposta indica que a atualização foi bem sucedido
    And o cartao de nome "Visa", numero_cartao "5410 9876 5432 1098", cvv "937" e validade "2027-08-20" está cadastrado