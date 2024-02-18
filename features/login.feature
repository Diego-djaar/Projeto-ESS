Feature: Login 
As a usuário da plataforma de e-commerce 
I want to preencher os campos com email e senha 
So that eu posso acessar os serviços da plataforma 

Cenário: login bem sucedido 
Given o usuário 'Gabriel' está na página 'Fazer login'
And 'Gabriel' está cadastrado na plataforma com nome 'Gabriel', sobrenome 'Silva', CPF '111.222.333-44', endereço 'Rua alameda sempre verde', CEP '12345-678', data de nascimento '17/06/2003', email 'usuario@gmail.com' e senha '12345678a'. 
When 'Gabriel' preenche os campos disponíveis com o email 'usuario@gmail.com' e senha '12345658b'
And seleciona a opção 'Submeter'
Then “Gabriel” visualiza a  página inicial da plataforma. 


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

Scenario: login mal sucedido devido a senha incorreta
Given 'Gabriel' está na página 'Fazer login'
And 'Gabriel' está cadastrado na plataforma com nome 'Gabriel', sobrenome 'Silva', CPF '111.222.333-44', endereço 'Rua alameda sempre verde', CEP '12345-678', data de nascimento '17/06/2003', email 'usuario@gmail.com' e senha '12345678a'. 
When 'Gabriel' preenche os campos disponíveis com o email 'usuario@gmail.com' e senha '12345658b'
And seleciona a opção 'Submeter'
Then 'Gabriel' visualiza a mensagem 'usuário ou senha incorreto'
And permanece na página 'Fazer login' 


Scenario: login mal sucedido devido a email incorreto
Given 'Gabriel' está na página 'Fazer login' 
And 'Gabriel' está cadastrado na plataforma com nome 'Gabriel', sobrenome 'Silva', CPF '111.222.333-44', endereço 'Rua alameda sempre verde', CEP '12345-678', data de nascimento '17/06/2003', email 'usuario@gmail.com' e senha '12345678a'. 
When 'Gabriel' preenche os campos disponíveis com o email 'usuario@gmail.com' e senha '12345658b'
And seleciona a opção 'Submeter'
Then 'Gabriel' visualiza a mensagem 'usuário ou senha incorreto'
And permanece na página 'Fazer login' 


Scenario: processar dados de login
Given Usuário "Gabriel" está cadastrado
When uma requisição "POST" for enviada para "login", com "Dados Login"
And a requisição está com o campo "Senha" correto
Then o status da resposta deve ser "200"
And o campo "data" possui o campo "token" com valor "$token_valor"
When uma requisição "POST" for enviada para "verify", com "$token_valor"
Then o status da resposta deve ser "200"
And o campo "data" possui o campo "user"
And os elementos de "user" correspondem aos dados do usuário "Gabriel"

Scenario: processar dados de login com usuário inexistente
Given Usuário "Gabriel" não está cadastrado
When uma requisição "POST" for enviada para "login", com "Dados Login"
Then o status da resposta deve ser "401"
And o campo "message" tem o valor "CPF ou Senha incorretos"

Scenario: processar dados de login com senha incorreta
Given Usuário "Gabriel" não está cadastrado
When uma requisição "POST" for enviada para "login", com "Dados Login"
And a requisição está com o campo "Senha" incorreto
Then o status da resposta deve ser "401"
And o campo "message" tem o valor "CPF ou Senha incorretos"
