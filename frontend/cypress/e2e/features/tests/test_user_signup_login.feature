Feature: Cadastro e Login
As a usuário da plataforma de e-commerce
I want me cadastrar no sistema
So that eu preencha os campos de login com email e senha 
So that eu posso acessar os serviços da plataforma


Scenario: Ausência de cadastro ao Logar
Given Eu estou na página de "login"
And Usuário "Gabriel" não está cadastrado
When eu clico em "SignUp"
Then Eu sou redirecionado para a página de "signup"
And Eu preencho os dados: nome: "Gabriel", sobrenome: "Silva", user: "Gabriel", CPF: "111.222.333-44", endereço: "Rua alameda sempre verde", CEP: "12345-678", data de nascimento: "2003-06-17", email: "usuario@gmail.com", senha: "Xyzw3456"
When eu clico em "Cadastrar"
Then Eu sou redirecionado para a página de "user"

Scenario: Logar após Cadastro
Given Usuário "Enzo" não está cadastrado
And Eu não estou logado
And Eu estou na página de "signup"
When Eu preencho os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: "010.010.010-23", endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456"
And eu clico em "Cadastrar"
Then O cadastro é bem sucedido
When os cookies são limpos
And Eu estou na página de "login"
When Eu preencho no campo "CPF_ou_User_ou_Email" "EnzoGab@cin.ufpe.br"
And Eu preencho no campo "Senha" "Xyzw3456"
And eu clico em "Login"
Then Eu sou redirecionado para a página de "user"
And Estou logado como usuário "Enzo"