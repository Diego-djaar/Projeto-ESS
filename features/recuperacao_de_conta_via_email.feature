Feature: Recuperação de contas via e-mail / Esqueci a senha
As a um usuário que esqueceu a senha
I want to ser capaz de recuperar minha conta através do meu e-mail cadastrado
So that eu posso redefinir minha senha e acessar novamente minha conta.

Scenario: Recuperação de conta via e-mail cadastrado
Given "Peterson" está na página "Recuperar conta"
When "Peterson" preenche o campo disponível com seu email "peterson@gmail.com"
And seleciona a opção "Enviar código"
Then "Peterson" deve receber uma mensagem de confirmação de envio para o email fornecido
And "Peterson" é redirecionado para a página "Digitar código de recuperação".

Scenario: Recuperação de conta via e-mail não cadastrado
Given "Peterson" está na página "Recuperar conta"
When "Peterson" preenche o campo disponível com seu email "peterson2222@gmail.com" 
And o email "peterson2222@gmail.com" não está cadastrado no sistema
And seleciona a opção "Enviar código"
Then "Peterson" deve receber uma mensagem de informando que o email não está cadastrado
And "Peterson" permanece na página "Recuperar conta".

Scenario: Email de recuperação não recebido
Given "Peterson" está na página "Digitar código de recuperação"
And "Peterson" não recebeu o email de recuperação.
When "Peterson" seleciona a opção "Não recebi o email"
Then "Peterson" continua na mesma página
And recebe uma mensagem informando que o e-mail de recuperação foi reenviado.

Scenario: Código de recuperação correto
Given que "Peterson" está na página "Digitar código de recuperação"
When "Peterson" insere o código de recuperação recebido por e-mail
And o código está correto
And selecionar a opção "Enviar"
Then "Peterson" é redirecionado para a página "Redefinir Senha"

Scenario: Código de recuperação incorreto
Given que "Peterson" está na página "Digitar código de recuperação"
When "Peterson" insere o código de recuperação recebido por e-mail
And o código está incorreto
And selecionar a opção "Enviar"
Then "Peterson" recebe uma mensagem de erro indicando que o código é inválido
And permanece na página "Digitar código de recuperação".

Scenario: Redefinir a senha após verificação
Given que "Peterson" está na página "Redefinir Senha"
When "Peterson" insere a nova senha desejada
And confirma a nova senha
And seleciona a opção "Redefinir Senha"
Then recebe uma mensagem de confirmação informando que a senha foi redefinida com sucesso
And "Peterson" é redirecionado para a página de login.

Scenario: Nova senha não está nos padrões exigido
Given que "Peterson" está na página "Redefinir Senha"
When "Peterson" insere uma nova senha que não atende aos padrões exigidos
And confirma a nova senha
And clica no botão "Redefinir Senha"
Then "Peterson" permanece na mesma página
And recebe uma mensagem de erro informando que a nova senha não atende aos padrões exigidos.
