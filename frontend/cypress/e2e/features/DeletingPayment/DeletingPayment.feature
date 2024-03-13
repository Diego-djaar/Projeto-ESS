Feature: Deletando métodos de pagamento
    As a usuário 
    I want deleter os métodos de pagamento cadastrados
    so that eu posso remover os métodos de pagamento cadastrados no sistema 


Scenario: Deletando pix
    Given o usuário está na página "http://localhost:3123/paymentMethod"
    When o usuário clica no botão "delete_payment"
    And o usuário cujo pix de nome "Breno Gabriel de Melo Lima" e cpf "333.333.333-33" preenche o campo "delete_id" com o id do método e clica em "delete_button"
    Then o usuário visualiza a mensagem "Deleção realizada com sucesso"
    And o usuário é direcionando para a página "http://localhost:3123/paymentMethod"


Scenario: Deletando boleto 
    Given o usuário está na página "http://localhost:3123/paymentMethod"
    When o usuário clica no botão "delete_payment"
    And o usuário cujo boleto de nome "Breno Gabriel de Melo Lima" e cpf "333.333.333-33" preenche o campo "delete_id" com o id do método e clica em "delete_button"
    Then o usuário visualiza a mensagem "Deleção realizada com sucesso"
    And o usuário é direcionando para a página "http://localhost:3123/paymentMethod"


Scenario: Deletando cartão 
    Given o usuário está na página "http://localhost:3123/paymentMethod"
    When o usuário clica no botão "delete_payment"
    And o usuário cujo cartão de nome "MasterCard", numero  "4916538421959382", cvv "437", cpf "111.111.111-10", validade "2024-03-25" preenche o campo "delete_id" com o id do método e clica em "delete_button"
    Then o usuário visualiza a mensagem "Deleção realizada com sucesso"
    And o usuário é direcionando para a página "http://localhost:3123/paymentMethod"


Scenario: Deletando método com ID incorreto
    Given o usuário está na página "http://localhost:3123/paymentMethod"
    When o usuário clica no botão "delete_payment"
    And o usuário preenche o campo "delete_id" com o id incorreto do método e clica em "delete_button"
    Then o usuário visualiza a mensagem "ID não encontrado na base de dados"
    And o usuário é direcionando para a página "http://localhost:3123/paymentMethod"
