Feature: SignUp Service

# Service
    Scenario: Sign Up User
    Given Usuário com Cpf "123.123.123-45" não está cadastrado
    When o método de Sign Up é chamada com Dados Cadastrais username= "Maria", nome = "Maria", sobrenome = "Agra", cpf = "123.123.123-45", data_de_nascimento="datetime.datetime(1999,12,31)", email="Maria@proton.me", senha="12345XyzW", endereço = "None", CEP = "None"
    Then o método deve retornar que o Sign Up foi bem sucedido

    Scenario: Sign Up já existente
    Given Usuário com Cpf "123.123.123-45" está cadastrado
    When o método de Sign Up é chamada com Dados Cadastrais username= "Maria", nome = "Maria", sobrenome = "Agra", cpf = "123.123.123-45", data_de_nascimento="datetime.datetime(1999,12,31)", email="Maria@proton.me", senha="12345XyzW", endereço = "None", CEP = "None"
    Then o método deve retornar que o Sign Up foi mal sucedido
    And o campo "data" da resposta deve conter "Já existe uma conta com esse CPF"

    Scenario: Sign Up cpf mal formulado
    When o método de Sign Up é chamada com Dados Cadastrais username= "Maria", nome = "Maria", sobrenome = "Agra", cpf = "123.123", data_de_nascimento="datetime.datetime(1999,12,31)", email="Maria@proton.me", senha="12345XyzW", endereço = "None", CEP = "None"
    Then o método deve retornar que o Sign Up foi mal sucedido
    And o campo "data" da resposta deve conter "Campo CPF mal formulado"

