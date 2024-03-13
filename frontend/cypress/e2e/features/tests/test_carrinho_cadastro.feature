Feature: Cadastrar usuário e carrinho na base de dados
    As um usuário
    I want to me cadastrar no site
    So that eu possa decidir o que vou comprar e visualizar minhas escolhas no meu carrinho

    Scenario: Cadastrar usuário e criar um carrinho para o usuário
        Given o usuário está na página "signup"
        When Eu preencho os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: "010.010.010-23", endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456"
        Then o carrinho de CPF "010.010.010-23" é criado
        When o usuário está na página "carrinho"
        And o usuário coloca o CPF "010.010.010-23" no campo de visualizar carrinho
        And o usuário clica no botão de "Visualizar carrinho"
        Then o usuário vê um carrinho vazio