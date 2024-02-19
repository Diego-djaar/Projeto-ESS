Feature: Payment Methods Service 

#Service 
Scenario: Inserir cartão
    Given o cartao de nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.111-11" e validade "2025-02-17" não existe no banco de dados 
    When o método inserting_card do PaymentMethodService for chamado com Cartao("masterCard", número "4916123456789012", cvv "847", cpf "111.111.11-11" 
    e validade "datetime.datetime(2030,12,31)")
    Then o metodo insert_card retorna uma mensagem de confirmação
    And o cartao de nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.11" e validade "2024-02-17" existe no banco de dados 


# Scenario: Inserir cartão com cpf inválido
    Given o cartao de nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.11" e validade "2024-02-17" não existe no banco de dados 
    When o método inserting_card do PaymentMethodService for chamado com Cartao("masterCard", número "4916123456789012", cvv "847", cpf "111.111.11" 
    e validade "datetime.datetime(2030,12,31)")
    Then o metodo insert_card retorna uma mensagem informando a insucesso da operação 
    And o cartao de nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.11" e validade "2024-02-17" não existe no banco de dados 

Scenario: Inserir pix
    Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" não existe no banco de dados
    When o método insert_pix do PaymentDatabase for chamado com Pix(nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22")
    Then o metodo insert_pix retorna uma mensagem de confirmação
    And o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" existe no banco de dados

Scenario: Inserir pix com cpf inválido
    Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" não existe no banco de dados
    When o método insert_pix do PaymentDatabase for chamado com Pix(nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22")
    Then o metodo insert_pix retorna uma mensagem de confirmação
    And o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" existe no banco de dados

Scenario: Inserir boleto
    Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" não existe no banco de dados
    When o método insert_pix do PaymentDatabase for chamado com Pix(nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22")
    Then o metodo insert_pix retorna uma mensagem de confirmação
    And o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" existe no banco de dados

Scenario: Inserir boleto com cpf inválido
    Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" não existe no banco de dados
    When o método insert_pix do PaymentDatabase for chamado com Pix(nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22")
    Then o metodo insert_pix retorna uma mensagem de confirmação
    And o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" existe no banco de dados
