Feature: Payment Methods Service 

#Service 
Scenario: Inserir cartão
    Given o cartao de número "4916123456789012" e cpf "111.111.111-11" não existe no banco de dados 
    When o método inserting_card do PaymentMethodService for chamado com Cartao nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.111-11" e validade "2030-12-31"
    Then o metodo insert_card retorna uma mensagem de confirmação para o cartao de número "4916123456789012" e cpf "111.111.111-11"
    And o cartao de número "4916123456789012" e cpf "111.111.111-11" existe no banco de dados 


Scenario: Inserir cartão com cpf inválido
    Given o cartao de número "4916123456789012" e cpf "111.111.111" não existe no banco de dados 
    When o método inserting_card do PaymentMethodService for chamado com Cartao nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.111" e validade "2030-12-31"
    Then o metodo insert_card retorna uma mensagem de insucesso para o cartao de nome "MasterCard", número "4916123456789012", cvv "847" e cpf "111.111.111" e validade "2030-12-31"
    And o cartao de número "4916123456789012" e cpf "111.111.111" não existe no banco de dados 

Scenario: Inserir cartão fora da validade
    Given o cartao de número "4916123456789012" e cpf "111.111.111-11" não existe no banco de dados 
    When o método inserting_card do PaymentMethodService for chamado com Cartao nome "masterCard", número "4916123456789012", cvv "847", cpf "111.111.111-11" e validade "2020-12-31"
    Then o metodo insert_card retorna uma mensagem de insucesso para o cartao de nome "MasterCard", número "4916123456789012", cvv "847" e cpf "111.111.111-11" e validade "2020-12-31"
    And o cartao de número "4916123456789012" e cpf "111.111.111" não existe no banco de dados 

Scenario: Inserir cartão com numero inválido
    Given o cartao de número "4916123456789" e cpf "111.111.111" não existe no banco de dados 
    When o método inserting_card do PaymentMethodService for chamado com Cartao nome "masterCard", número "4916123456789", cvv "847", cpf "111.111.111" e validade "2030-12-31"
    Then o metodo insert_card retorna uma mensagem de insucesso para o cartao de nome "MasterCard", número "4916123456789", cvv "847" e cpf "111.111.111" e validade "2030-12-31"
    And o cartao de número "4916123456789012" e cpf "111.111.111" não existe no banco de dados 

Scenario: Inserir pix
    Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" não existe no banco de dados
    When o método insert_pix do PaymentDatabase for chamado com Pix nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22"
    Then o metodo insert_pix retorna uma mensagem de confirmação para o pix de cpf "222.222.222-22"
    And o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" existe no banco de dados

# Scenario: Inserir pix com cpf inválido
#     Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" não existe no banco de dados
#     When o método insert_pix do PaymentDatabase for chamado com Pix(nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22")
#     Then o metodo insert_pix retorna uma mensagem de confirmação
#     And o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" existe no banco de dados

# Scenario: Inserir boleto
#     Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" não existe no banco de dados
#     When o método insert_pix do PaymentDatabase for chamado com Pix(nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22")
#     Then o metodo insert_pix retorna uma mensagem de confirmação
#     And o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" existe no banco de dados

# Scenario: Inserir boleto com cpf inválido
#     Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" não existe no banco de dados
#     When o método insert_pix do PaymentDatabase for chamado com Pix(nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22")
#     Then o metodo insert_pix retorna uma mensagem de confirmação
#     And o pix de nome "Breno Gabriel de Melo Lima" e cpf "222.222.222-22" existe no banco de dados
