Feature: Cadastro e manutenção de usuários
As a usuário não cadastrado
I want me cadastrar no sistema
So that eu posso logar na plataforma e utilizar seus serviços


Scenario: Cadastro de usuário mal sucedido
Given Eu não estou logado
And Eu estou na página de "signup"
When Eu preencho os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: "010.010.010-23", endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456"
And Eu deixo o campo "Email" em branco
And eu clico em "Cadastrar"
Then O cadastro não é bem sucedido
And Eu sou notificado dos campos de cadastro que estão mal preenchidos

Scenario: Cadastro de usuário já existente
Given Usuário "Enzo" está cadastrado, com os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: "132.636.636-42", endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab1234@cin.ufpe.br", senha: "Xyzw3456"
And Eu não estou logado
And Eu estou na página de "signup"
When Eu preencho os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: "010.010.010-23", endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456"
And eu clico em "Cadastrar"
Then Eu sou notificado que o usuário "Enzo" já existe
And O cadastro não é bem sucedido
And Eu não estou logado

Scenario: Cadastro de usuário com CPF já existente
Given Usuário "Enzo" está cadastrado, com os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: "111.111.111-11", endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456"
And Eu estou na página de "signup"
When Eu preencho os dados: nome: "Gabriel", Sobrenome: "Silva", User: "Gab", data de nascimento: "2001-01-01", email: "Gabriel@cin.ufpe.br", senha: "Abcd9678"
And Eu preencho no campo "CPF" "111.111.111-11"
And eu clico em "Cadastrar"
Then Eu sou notificado que o usuário com esse "CPF" já existe
And Eu não estou logado

Scenario: Cadastro de usuário com Senha não atendendo aos requisitos
Given Usuário "Enzo" não está cadastrado
And Eu não estou logado
And Eu estou na página de "signup"
When Eu preencho os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: "010.010.010-23", endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456"
And Eu preencho no campo "Repetir_Senha" "1234" 
And Eu preencho no campo "Senha" "1234"
And eu clico em "Cadastrar"
Then O cadastro não é bem sucedido
And Eu sou notificado dos campos de cadastro que estão mal preenchidos

Scenario: Cadastro de usuário bem sucedido
Given Usuário "Enzo" não está cadastrado
And Eu não estou logado
And Eu estou na página de "signup"
When Eu preencho os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: "010.010.010-23", endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456"
And eu clico em "Cadastrar"
Then O cadastro é bem sucedido
And Eu sou redirecionado para a página de "user"
And Estou logado como usuário "Enzo"