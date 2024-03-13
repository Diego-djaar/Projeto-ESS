Feature: Login 
As a usuário da plataforma de e-commerce 
I want to preencher os campos com email e senha 
So that eu posso acessar os serviços da plataforma 

Scenario: login bem sucedido 
Given Eu estou na página de "login"
And Usuário "Gabriel" está cadastrado, com os dados: nome: "Gabriel", sobrenome: "Silva", user: "Gabriel", CPF: "111.222.333-44", endereço: "Rua alameda sempre verde", CEP: "12345-678", data de nascimento: "2003-06-17", email: "usuario@gmail.com", senha: "Xyzw3456"
When Eu preencho no campo "CPF_ou_User_ou_Email" "usuario@gmail.com"
And Eu preencho no campo "Senha" "Xyzw3456"
And eu clico em "Login"
Then o login é bem sucedido
And Eu sou redirecionado para a página de "user"

# integração com feature esquecer senha
# Scenario: Esquecimento de senha
# Given "Gabriel" está na página de login 
# And "Gabriel" esqueceu a senha de login
# When "Gabriel" seleciona a opção "esqueci minha senha"
# And preenche os campos com o cpf "000000000-00" e a nova senha "abcde345"
# And seleciona "redefinir senha"
# Then "Gabriel" visualiza a mensagem "senha redefinida"
# And retorna para a página de login 

Scenario: login mal sucedido devido a senha incorreta
Given Eu estou na página de "login"
And Usuário "Gabriel" está cadastrado, com os dados: nome: "Gabriel", sobrenome: "Silva", user: "Gabriel", CPF: "111.222.333-44", endereço: "Rua alameda sempre verde", CEP: "12345-678", data de nascimento: "2003-06-17", email: "usuario@gmail.com", senha: "Xyzw3456"
When Eu preencho no campo "CPF_ou_User_ou_Email" "usuario2@gmail.com"
And Eu preencho no campo "Senha" "4245235"
And eu clico em "Login"
Then Eu visualizo a mensagem "CPF ou Senha incorretos"
And permanece na página "login" 


Scenario: login mal sucedido devido a email incorreto
Given Eu estou na página de "login"
And Usuário "Gabriel" está cadastrado, com os dados: nome: "Gabriel", sobrenome: "Silva", user: "Enzo", CPF: "111.222.333-44", endereço: "Rua alameda sempre verde", CEP: "12345-678", data de nascimento: "2003-06-17", email: "usuario@gmail.com", senha: "Xyzw3456"
When Eu preencho no campo "CPF_ou_User_ou_Email" "usuario2@gmail.com"
And Eu preencho no campo "Senha" "Xyzw3456"
And eu clico em "Login"
Then Eu visualizo a mensagem "CPF ou Senha incorretos"
And permanece na página "login" 