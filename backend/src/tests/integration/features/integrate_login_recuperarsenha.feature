Feature: Integrar User Login e Recuperar Senha

    Scenario: Logar após recuperar Senha
    Given Usuário com Cpf "111.111.111-02" está cadastrado
    And o usuário possui a senha "faculdade123"
    And o usuário possui o campo "email" o valor "djaar@cin.ufpe.br"
    When o método Login User é chamado com DadosLogin(cpf_ou_user_ou_email="111.111.111-02", senha="12345Abcx")
    Then o método deve retornar que o login foi mal sucedido
    When o método Enviar Email é chamado com email: "djaar@cin.ufpe.br"
    And o método Recuperar Conta é chamado com email: "djaar@cin.ufpe.br", código válido e nova senha "faculdade124"
    Then Usuário com Cpf "111.111.111-02" está cadastrado
    And o usuário possui a senha "faculdade124"
    When o método Login User é chamado com DadosLogin(cpf_ou_user_ou_email="111.111.111-02", senha="faculdade124")
    Then o método deve retornar que o login foi bem sucedido