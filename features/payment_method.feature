Feature: Cadastro e manutenção de métodos de pagamento (inserir, remover, atualizar)
As a usuário cadastrado
I want inserir, remover ou atualizar os métodos de pagamento
So that eu posso realizar o pagamento de minhas compras

Scenario: Inserção bem-sucedida de boleto como método de pagamento
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "inserir método de pagamento"
And seleciona o a opção "Boleto"
And  preencher o campo "Nome completo" com "Breno Gabriel de Melo Lima"
And preencher o campo "CPF" com "925.830.910-34"
And o usuário clica em "Confirmar"
Then o método de pagamento será cadastrado no sistema 

Scenario: Inserção bem-sucedida de Pix como método de pagamento 
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "inserir método de pagamento"
And seleciona o a opção "Pix"
And  preencher o campo "Nome completo" com "Breno Gabriel de Melo Lima"
And preencher o campo "CPF" com "925.830.910-34"
And o usuário clica em "Confirmar"
Then o método de pagamento será cadastrado no sistema 

Scenario: Inserção bem-sucedida de cartão como método de pagamento 
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "inserir método de pagamento"
And seleciona o a opção "Cartão"
And preencher o campo "Nome do cartão" com "Nubank"
And preencher o campo "CPF" com "925.830.910-34"
And  preencher o campo "CVV" com "1234"
And  preencher o campo "Número do cartão" com "12345678"
And  preencher o campo "Validade" com "06/2028"
And o usuário clica em "Confirmar"
Then o método de pagamento será cadastrado no sistema 

Scenario: Inserção mal-sucedida de boleto como método de pagamento
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "inserir método de pagamento"
And seleciona o a opção "Boleto"
And  preencher o campo "Nome completo" com "Breno Gabriel de Melo Lima"
And preencher o campo "CPF" com "925.830.910"
And o usuário clica em "Confirmar"
Then o usuário visualiza a mensagem "Informações inválidas"

Scenario: Inserção mal-sucedida de Pix como método de pagamento
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "inserir método de pagamento"
And seleciona o a opção "Boleto"
And  preencher o campo "Nome completo" com "Breno Gabriel de Melo Lima"
And preencher o campo "CPF" com "925.830.910"
And o usuário clica em "Confirmar"
Then o usuário visualiza a mensagem "Informações inválidas"

Scenario: Inserção mal-sucedida de cartão como método de pagamento devido a CPF inválido
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "inserir método de pagamento"
And seleciona o a opção "Cartão"
And preencher o campo "Nome do cartão" com "Nubank"
And preencher o campo "CPF" com "925.830.910"
And  preencher o campo "CVV" com "1234"
And  preencher o campo "Número do cartão" com "12345678"
And  preencher o campo "Validade" com "06/2028"
And o usuário clica em "Confirmar"
Then o usuário visualiza a mensagem "Informações inválidas" 

Scenario: Inserção mal-sucedida de cartão como método de pagamento devido a CVV inválido
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "inserir método de pagamento"
And seleciona o a opção "Cartão"
And preencher o campo "Nome do cartão" com "Nubank"
And preencher o campo "CPF" com "925.830.910-34"
And  preencher o campo "CVV" com "123"
And  preencher o campo "Número do cartão" com "12345678"
And  preencher o campo "Validade" com "06/2028"
And o usuário clica em "Confirmar"
Then o usuário visualiza a mensagem "Informações inválidas" 

Scenario: Inserção mal-sucedida de cartão como método de pagamento devido a número de cartão inválido
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "inserir método de pagamento"
And seleciona o a opção "Cartão"
And preencher o campo "Nome do cartão" com "Nubank"
And preencher o campo "CPF" com "925.830.910"
And  preencher o campo "CVV" com "1234"
And  preencher o campo "Número do cartão" com "123456"
And  preencher o campo "Validade" com "06/2028"
And o usuário clica em "Confirmar"
Then o usuário visualiza a mensagem "Informações inválidas" 

Scenario: Inserção mal-sucedida de cartão como método de pagamento devido a data de validade inválida 
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "inserir método de pagamento"
And seleciona o a opção "Cartão"
And preencher o campo "Nome do cartão" com "Nubank"
And preencher o campo "CPF" com "925.830.910"
And  preencher o campo "CVV" com "1234"
And  preencher o campo "Número do cartão" com "12345678"
And  preencher o campo "Validade" com "06/2020"
And o usuário clica em "Confirmar"
Then o usuário visualiza a mensagem "Informações inválidas" 

Scenario: Atualização bem-sucedida de informações do cartão
Given o usuário de email "usuário@gmail.com" está na página "Métodos de pagamento"
When usuário clicar na opção "atualizar método de pagamento"
And selecionar a opção "nubank"
And atualizar o campo "Nome completo" com "Maria Alvez da Cunha"
And o usuário clica em "Confirmar"
Then o usuário visualiza a mensagem "Informações atualizadas"
