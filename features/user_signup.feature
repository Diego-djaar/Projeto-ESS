Feature: Cadastro e manutenção de usuários
As a usuário não cadastrado
I want me cadastrar no sistema
So that eu posso logar na plataforma e utilizar seus serviços


Cenário: Cadastro de usuário mal sucedido
Given Usuário "Enzo” não está cadastrado
And Eu não estou logado
And Eu estou na página de "Cadastro”
When Eu preencho os dados: (nome: “Enzo Gabriel“, sobrenome: “Rocha“, user: “Enzo“, CPF: 010.010.010-23, endereço:  “Av. Dois Rios, 74 - Ibura, Recife - PE nº 700“, CEP: “51230-000“, data de nascimento: “02/02/2002“, email: “EnzoGab@cin.ufpe.br“, senha: “Xyzw3456“)
And Eu deixo o campo "Email" em branco
And eu clico em "Cadastrar"
Then O cadastro não é bem sucedido
And Eu sou notificado dos campos de cadastro que estão mal preenchidos

Cenário: Cadastro de usuário já existente
Given Usuário "Enzo” está cadastrado
And Eu não estou logado
And Eu estou na página de "Cadastro”
And Eu preencho no campo "User" "Enzo"
When Eu preencho os dados: (nome: “Enzo Gabriel“, sobrenome: “Rocha“, user: “Enzo“, CPF: 010.010.010-23, endereço:  “Av. Dois Rios, 74 - Ibura, Recife - PE nº 700“, CEP: “51230-000“, data de nascimento: “02/02/2002“, email: “EnzoGab@cin.ufpe.br“, senha: “Xyzw3456“)
And eu clico em "Cadastrar"
Then Eu sou notificado que o usuário "Enzo” já existe
And Eu sou redirecionado para a página de "Login”
And eu não estou logado

Cenário: Cadastro de usuário com CPF já existente
Given Usuário "Enzo” está cadastrado
And Usuário "Enzo" tem CPF "111.111.111-11"
And Eu estou na página de "Cadastro”
When Eu preencho os dados: (Nome: “Gabriel”, Sobrenome: “Silva”, User: “Gab”, data de nascimento: 01/01/2001, email: “Gabriel@cin.ufpe.br”, senha: “Abcd9678”)
And Eu preencho no campo "CPF" "111.111.111-11"
And eu clico em "Cadastrar"
Then Eu sou notificado que o usuário com esse “CPF” já existe
And Eu sou redirecionado para a página de "Login”
And eu não estou logado

Cenário: Cadastro de usuário com Senha não atendendo aos requisitos
Given Usuário "Enzo” não está cadastrado
And Eu não estou logado
And Eu estou na página de "Cadastro”
When Eu preencho os dados: (nome: “Enzo Gabriel“, sobrenome: “Rocha“, user: “Enzo“, CPF: 010.010.010-23, endereço:  “Av. Dois Rios, 74 - Ibura, Recife - PE nº 700“, CEP: “51230-000“, data de nascimento: “02/02/2002“, email: “EnzoGab@cin.ufpe.br“, senha: “Xyzw3456“)
And Eu preencho "1234" no campo senha
And eu clico em "Cadastrar"
Then O cadastro não é bem sucedido
And Eu sou notificado dos campos de cadastro que estão mal preenchidos

Cenário: Cadastro de usuário bem sucedido
Given Usuário "Enzo” não está cadastrado
And Eu não estou logado
And Eu estou na página de "Cadastro”
When Eu preencho os dados: (nome: “Enzo Gabriel“, sobrenome: “Rocha“, user: “Enzo“, CPF: 010.010.010-23, endereço:  “Av. Dois Rios, 74 - Ibura, Recife - PE nº 700“, CEP: “51230-000“, data de nascimento: “02/02/2002“, email: “EnzoGab@cin.ufpe.br“, senha: “Xyzw3456“)
And eu clico em "Cadastrar"
Then O cadastro é bem sucedido
And Eu sou redirecionado para a página "Página Principal”
And A conta de "Enzo” é um "Usuário comum"
And Estou logado como usuário “Enzo“

Cenário: Processar dados cadastrais bem sucedido
Given Usuário "Enzo" não está cadastrado
When uma requisição "POST" for enviada para "login", com "Dados Cadastrais"
And a requisição está correta
And o campo "Nome" da requisição é "Enzo Gabriel" e o campo "sobrenome" é "de Oliveira"
And o campo "Username" é "Enzo"
Then o campo "CPF" da requisição é validado
And o campo "Data_de_nascimento" da requisição é validado
And o campo "Email" da requisição é validado
Then o status da resposta deve ser "200"
And o JSON da resposta indica que o cadastro foi bem sucedido
And Usuário "Enzo" está cadastrado
And a conexão é autenticada como usuário "Enzo"

Cenário: Processar dados cadastrais mal sucedido
Given Usuário "Enzo" não está cadastrado
When uma requisição "POST" for enviada para "login", com "Dados Cadastrais"
And a requisição está com o campo "CPF" com "00.00.00"
Then o campo "CPF" da requisição é rejeitado
Then o status da resposta deve ser "200"
And o JSON da resposta indica que o cadastro foi mal sucedido
And o JSON da resposta indica que o campo "CPF" foi mal preenchido

Cenário: Remoção de usuário
Given eu sou usuário "Administrador"
And Usuário "Enzo" está cadastrado
And estou na página "Administração"
When eu insiro o comando para "Remover usuário Enzo"
Then Usuário "Enzo" não está cadastrado

