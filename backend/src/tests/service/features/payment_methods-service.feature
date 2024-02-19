Feature: Payment Methods Service 

#Service 
Scenario: Inserir cartão
    # Given o cartao de nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.11-11" e validade "2024-02-17" não existe no banco de dados 
    Given o método inserting_card do PaymentMethodService retorna um json com message "método cadastrado com sucesso" e status_code = "201"
    And o cartao "cartao" nao existe no banco de dados 
    When o método inserting_card do PaymentMethodService for chamado com cartao "cartao"
    Then o cartao "cartao" for criado com sucesso 


Scenario: Inserir cartão com cpf inválido
    Given o cartao de nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.11" e validade "2024-02-17" não existe no banco de dados 
    When o método insert_card do PaymentDatabase for chamado com nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.111" e validade "2024-02-17"
    Then o método insert_card do PaymentDatabase retorna sucess "True" e problemas = "[CPF]"

Scenario: Inserir pix
    Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" não existe no banco de dados
    When o método insert_pix do PaymentDatabase for chamado com nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" 
    Then o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" foi criado com sucesso
    And o método insert_pix do PaymentDatabase retorna sucess "True"

Scenario: Inserir pix com cpf incorreto
    Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222" não existe no banco de dados
    When o método insert_pix do PaymentDatabase for chamado com nome "Breno Gabriel de Melo Lima" e cpf "222.222.222" 
    Then o método insert_pix do PaymentDatabase retorna sucess "False"
