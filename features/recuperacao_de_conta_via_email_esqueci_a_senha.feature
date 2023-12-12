Feature: Recuperação de conta via email / esqueci a senha
    As a Usuario
    I want to Recuperar minha conta via email pois esqueci a senha
    So that Eu posso ter o acesso da minha conta novamente

Scenario: Usuario esqueceu a senha
    Given o usuario "Peterson Melo" esqueceu a senha
    When o usuario acessa a pagina de recuperacao AND insere seu email
    Then o sistema deve enviar um email com um link para redifinir a senha para "petersonMelo@gmail.com"

Scenario: 