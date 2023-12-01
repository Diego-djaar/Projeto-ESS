Feature: Cadastro e manutenção de usuários
As a usuário não cadastrado
I want me cadastrar no sistema
So that eu posso logar na plataforma e utilizar seus serviços


Cenário: Cadastro de usuário mal sucedido
Given Usuário “Enzo” não está cadastrado
And Eu não estou logado
And Eu estou na página de “Cadastro”
When Eu preencho os “Dados Cadastrais” incorretamente
Then O cadastro não é bem sucedido
And Eu sou notificado dos campos de cadastro que estão mal preenchidos


Cenário: Cadastro de usuário já existente
Given Usuário “Enzo” está cadastrado
And Eu não estou logado
And Eu estou na página de “Cadastro”
When Eu preencho os “Dados Cadastrais”
Then Eu sou notificado que o usuário “Enzo” já existe
And Eu sou redirecionado para a página de “Login”


Cenário: Cadastro de usuário bem sucedido
Given Usuário “Enzo” não está cadastrado
And Eu não estou logado
And Eu estou na página de “Cadastro”
When Eu preencho os “Dados Cadastrais” corretamente // Dados cadastrais possui nome, sobrenome, CPF, endereço (opcional), CEP (opcional), data de nascimento, email e senha para login
Then O cadastro é bem sucedido
And Eu sou redirecionado para a página “Página Principal”
And A conta de “Enzo” é um “Usuário comum”