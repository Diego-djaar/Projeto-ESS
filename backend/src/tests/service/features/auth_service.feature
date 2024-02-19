Feature: Auth Service

# Service
    Scenario: login user
    Given Usuário com Cpf "444.324.424-09" está cadastrado
    And o usuário possui a senha "12345Abcx"
    When o método Login User é chamado com DadosLogin(cpf_ou_user_ou_email="444.324.424-09", senha="12345Abcx")
    Then o método deve retornar que o login foi bem sucedido
    And o campo "data" da resposta deve conter o campo "token"

    Scenario: login user fail
    Given Usuário com Cpf "444.324.424-09" está cadastrado
    And o usuário possui a senha "12345Abcx"
    When o método Login User é chamado com DadosLogin(cpf_ou_user_ou_email="444.324.424-09", senha="12345Abcz")
    Then o método deve retornar que o login foi mal sucedido
    And o campo "message" da resposta deve conter o valor "CPF ou Senha incorretos"

    Scenario: login user fail 2
    Given Usuário com Cpf "443.324.424-09" não está cadastrado
    When o método Login User é chamado com DadosLogin(cpf_ou_user_ou_email="443.324.424-09", senha="12345Abcx")
    Then o método deve retornar que o login foi mal sucedido
    And o campo "message" da resposta deve conter o valor "CPF ou Senha incorretos"
    