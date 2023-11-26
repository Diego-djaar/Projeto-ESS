Feature: Login 
As a usuário da plataforma de e-commerce 
I want to preencher os campos com email e senha 
So that eu posso acessar os serviços da plataforma 

Scenario: login bem sucedido 
Given “Gabriel” está na página de login 
When “Gabriel”preenche os campos disponíveis com seu login “gabriel_lopes123” e senha “12345678abc”
And seleciona a opção “Login”
Then “Gabriel” visualiza a página inicial da plataforma.  

Scenario: login mal sucedido devido a informações incorretas 
Given “Gabriel” está na página de login 
When “Gabriel”preenche os campos disponíveis com seu login “gabriel_lopes123” e senha “12345678abc”
And seleciona a opção “Login”
Then “Gabriel” visualiza a mensagem “e-mail ou senha incorreto”
And permanece na pagina de login 

Scenario: Esquecimento de senha
Given “Gabriel” está na página de login 
And “Gabriel” esqueceu a senha de login
When “Gabriel” seleciona a opção “esqueci minha senha”
And preenche os campos com o cpf “000000000-00” e a nova senha “abcde345”
And seleciona “redefinir senha”
Then “Gabriel” visualiza a mensagem “senha redefinida”
And retorna para a página de login 

Scenario: Ausência de cadastro
Given “Gabriel” está na página de login 
And “Gabriel” não tem nenhum cadastro na plataforma 
When “Gabriel” seleciona a opção “Não tem uma conta ?!”
And preenche os campos com seu nome “Gabriel” , sobrenome “Lopes” , CPF “000000000-00”, endereço: “Rua alameda sempre verde”, CEP “XXXXXXXX”, data de nascimento “20/06/2001” , email “XXXXXXXXXXXX@gmail.com”  e a senha “123456yuytre ”. 
And “Gabriel” seleciona a opção “realizar cadastro”
Then “Gabriel” visualiza a mensagem “Cadastro realizado”
And “Gabriel” é direcionado para a “página inicial” da plataforma
And "Gabriel" visualiza a página "lista de ofertas"

Scenario: login mal-sucedido devido a senha incorreta 
Given "Gabriel" está na página "Fazer login"
And "Gabriel" tem o seu nome “Gabriel” , sobrenome “Lopes” , CPF “000000000-00”, endereço: “Rua alameda sempre verde”, CEP “XXXXXXXX”, data de nascimento “20/06/2001” , email “XXXXXXXXXXXX@gmail.com”  e a senha “123456yuytre” armazenados no banco de dados. 
When "Gabriel" preenche os campos com seu email "XXXXXXXXXXXX@gmail.com" e senha "12345uyureea"
Then "Gabriel" visualiza a mensagem: "Email e/ou senha incorretos"
And permanece na página "fazer login"

Scenario: login mal-sucedido devido a email incorreto 
Given "Gabriel" está na página "Fazer login"
And "Gabriel" tem o seu nome “Gabriel” , sobrenome “Lopes” , CPF “000000000-00”, endereço: “Rua alameda sempre verde”, CEP “XXXXXXXX”, data de nascimento “20/06/2001” , email “teste@gmail.com”  e a senha “123456yuytre” armazenados no banco de dados. 
When "Gabriel" preenche os campos com seu email "teste_errado@gmail.com" e senha "123456yuytre"
Then "Gabriel" visualiza a mensagem: "Email e/ou senha incorretos"
And permanece na página "fazer login"