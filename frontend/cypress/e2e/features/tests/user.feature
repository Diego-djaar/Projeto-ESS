Feature: Usuário
As a usuário cadastrado
I want to acessar a página de usuário
So that eu posso configurar a minha conta

Scenario: deslogar da conta
Given Eu estou na página de "login"
And Usuário "Gabriel" está cadastrado, com os dados: nome: "Gabriel", sobrenome: "Silva", user: "Gabriel", CPF: "111.222.333-44", endereço: "Rua alameda sempre verde", CEP: "12345-678", data de nascimento: "2003-06-17", email: "usuario@gmail.com", senha: "Xyzw3456"
When Eu preencho no campo "CPF_ou_User_ou_Email" "usuario@gmail.com"
And Eu preencho no campo "Senha" "Xyzw3456"
And eu clico em "Login"
Then o login é bem sucedido
And Eu sou redirecionado para a página de "user"
When eu clico em "Unlogin"
Then Eu sou redirecionado para a página de "login"
And Eu não estou logado

Scenario: excluir usuário
Given Eu estou na página de "login"
And Usuário "Gabriel" está cadastrado, com os dados: nome: "Gabriel", sobrenome: "Silva", user: "Gabriel", CPF: "111.222.333-44", endereço: "Rua alameda sempre verde", CEP: "12345-678", data de nascimento: "2003-06-17", email: "usuario@gmail.com", senha: "Xyzw3456"
When Eu preencho no campo "CPF_ou_User_ou_Email" "usuario@gmail.com"
And Eu preencho no campo "Senha" "Xyzw3456"
And eu clico em "Login"
Then o login é bem sucedido
And Eu sou redirecionado para a página de "user"
When eu clico em "Exclude"
Then Eu sou redirecionado para a página de "login"
And Eu não estou logado
And Usuário "Gabriel" não está mais cadastrado

Scenario: alterar dados de usuário
Given Eu estou na página de "login"
And Usuário "Gabriel" está cadastrado, com os dados: nome: "Gabriel", sobrenome: "Silva", user: "Gabriel", CPF: "111.222.333-44", endereço: "Rua alameda sempre verde", CEP: "12345-678", data de nascimento: "2003-06-17", email: "usuario@gmail.com", senha: "Xyzw3456"
When Eu preencho no campo "CPF_ou_User_ou_Email" "usuario@gmail.com"
And Eu preencho no campo "Senha" "Xyzw3456"
And eu clico em "Login"
Then o login é bem sucedido
And Eu sou redirecionado para a página de "user"
When eu clico em "Update"
Then Eu sou redirecionado para a página de "update_user"
And Eu preencho no campo "Sobrenome" "Lima" 
When eu clico em "UpdateUser"
And Eu sou redirecionado para a página de "user"
And vejo no campo "Sobrenome" "Sobrenome: Lima"
