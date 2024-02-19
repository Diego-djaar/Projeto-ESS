Feature: User

    Scenario: Criação de novo usuário
    When é criado um novo user com os dados User(username="Enzo", nome="Enzo Gabriel", sobrenome="de Oliveira", cpf="111.111.111-11", data_de_nascimento="datetime.date.fromisocalendar(2001,1,1)", email="ego@cin.ufpe.br", senha="12345Abcx")
    Then a criação do user é bem sucedida
    And o user possui a senha "12345Abcx"

    Scenario: Criação de novo usuário falha
    When é criado um novo user com os dados User(username="Enzo", nome="Enzo Gabriel", sobrenome="de Oliveira", cpf="111.111", data_de_nascimento="datetime.date.fromisocalendar(2001,1,1)", email="_", senha="_")
    Then a criação do user é mal sucedida
    And "EMAIL" está na razão da falha
    And "CPF" está na razão da falha
    And "SENHA" está na razão da falha

    Scenario: Adição do usuário a base de dados
    When é criado um novo user com os dados User(username="stringw3532fgq", nome="string", sobrenome="sting", cpf="123.156.185-21", data_de_nascimento="datetime.datetime(1,1,1)", email="string@s", senha="string123", endereço="string", CEP="01010-142")
    And o user é adicionado a base de dados
    Then Usuário "stringw3532fgq" está cadastrado

    Scenario: Adição falha de usuário a base de dados
    Given Usuário com Email "luis14@proton.me" está cadastrado
    When é criado um novo user com os dados User(username="LOUIS XIV", nome="Luis", sobrenome="XIV", cpf="141.414.141-14", "data_de_nascimento=datetime.datetime(1643,5,14)", email="luis14@proton.me", senha="senha1234")
    

