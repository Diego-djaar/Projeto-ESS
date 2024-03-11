Feature: Inserir método de pagamento
    As a usuário 
    I want inserir novos métodos de pagamento 
    so that eu posso ter novos métodos de pagamento em meu perfil

Scenario: Inserir Pix corretamente 
    Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "111.111.111-11" não está cadastrado no sistema 
    And o usuário está na página "http://localhost:3000/paymentMethod"
    When o usuário clica no botão "insert_payment"
    And o usuário clica no botão "select_pix"
    And o usuário preenche o campo "inserir_nome_pix" com "Breno gabriel de Melo Lima", o campo "inserir_cpf_pix" com "111.111.111-11" e clica no botão "inserir_pix_botao"
    Then o usuário visualiza a mensagem "metodo de pagamento cadastrado com sucesso"
    And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/inserting"

Scenario: Inserir Pix que já foi cadastrado
    Given o pix de nome "Breno Gabriel de Melo Lima" e cpf "111.111.111-11" está cadastrado no sistema 
    And o usuário está na página "http://localhost:3000/paymentMethod"
    When o usuário clica no botão "insert_payment"
    And o usuário clica no botão "select_pix"
    And o usuário preenche o campo "inserir_nome_pix" com "Maria Edna Francisco", o campo "inserir_cpf_pix" com "111.111.111-11" e clica no botão "inserir_pix_botao"
    Then o usuário visualiza a mensagem "Já existe um pix cadastrado no sistema"

Scenario: Inserir Pix com valor de CPF incorreto 
    Given o usuário está na página "http://localhost:3000/paymentMethod"
    When o usuário clica no botão "insert_payment"
    And o usuário clica no botão "select_pix"
    And o usuário preenche o campo "inserir_nome_pix" com "Maria Francisco Teixeira", o campo "inserir_cpf_pix" com "222.222.222-22" e clica no botão "inserir_pix_botao"
    Then o usuário visualiza a mensagem "Informações inválidas"

Scenario: Inserir Boleto corretamente 
    Given o boleto de nome "Breno Gabriel de Melo Lima" e cpf "111.111.111-11" não está cadastrado no sistema 
    And o usuário está na página "http://localhost:3000/paymentMethod"
    When o usuário clica no botão "insert_payment"
    And o usuário clica no botão "select_boleto"
    And o usuário preenche o campo "inserir_nome_boleto" com "Breno gabriel de Melo Lima", o campo "inserir_cpf_boleto" com "111.111.111-11" e clica no botão "inserir_boleto_botao"
    Then o usuário visualiza a mensagem "metodo de pagamento cadastrado com sucesso"
    And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/inserting"


Scenario: Inserir Boleto que já foi cadastrado
    Given o boleto de nome "Breno Gabriel de Melo Lima" e cpf "111.111.111-11" está cadastrado no sistema 
    And o usuário está na página "http://localhost:3000/paymentMethod"
    When o usuário clica no botão "insert_payment"
    And o usuário clica no botão "select_boleto"
    And o usuário preenche o campo "inserir_nome_boleto" com "Breno gabriel de Melo Lima", o campo "inserir_cpf_boleto" com "111.111.111-11" e clica no botão "inserir_boleto_botao"
    Then o usuário visualiza a mensagem "Já existe um boleto cadastrado no sistema"

Scenario: Inserir Boleto com cpf incorreto 
    Given o usuário está na página "http://localhost:3000/paymentMethod"
    When o usuário clica no botão "insert_payment"
    And o usuário clica no botão "select_boleto"
    And o usuário preenche o campo "inserir_nome_boleto" com "Breno gabriel de Melo Lima", o campo "inserir_cpf_boleto" com "111.111.111" e clica no botão "inserir_boleto_botao"
    Then o usuário visualiza a mensagem "Informações inválidas"

# Scenario: Inserir Cartao corretamente 
#     Given o usuário está na página "http://localhost:3000/paymentMethod"
#     When o usuário clica no botão "insert_payment"
#     And o usuário clica no botão "select_cartao"
#     And o usuário preenche o campo "inserir_nome_cartao" com "MasterCard", o campo "inserir_numero_cartao" com "4916538421959382", o campo "inserir_cvv" com "437", o campo "inserir_cpf_cartao" com "111.111.111-11", o campo "inserir_validade" com "2024-03-25" e clica no botão "inserir_cartao_botao"
#     Then o usuário visualiza a mensagem "metodo de pagamento cadastrado"
#     And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/inserting"

Scenario: Inserir Cartao com número inválido
    Given o usuário está na página "http://localhost:3000/paymentMethod"
    When o usuário clica no botão "insert_payment"
    And o usuário clica no botão "select_cartao"
    And o usuário preenche o campo "inserir_nome_cartao" com "MasterCard", o campo "inserir_numero_cartao" com "8394204850258390", o campo "inserir_cvv" com "437", o campo "inserir_cpf_cartao" com "111.111.111-11", o campo "inserir_validade" com "2024-03-25" e clica no botão "inserir_cartao_botao"
    Then o usuário visualiza a mensagem "Informações inválidas"

Scenario: Inserir Cartao com cpf inválido
    Given o usuário está na página "http://localhost:3000/paymentMethod"
    When o usuário clica no botão "insert_payment"
    And o usuário clica no botão "select_cartao"
    And o usuário preenche o campo "inserir_nome_cartao" com "MasterCard", o campo "inserir_numero_cartao" com "8394204850258390", o campo "inserir_cvv" com "437", o campo "inserir_cpf_cartao" com "111.111.111", o campo "inserir_validade" com "2024-03-25" e clica no botão "inserir_cartao_botao"
    Then o usuário visualiza a mensagem "Informações inválidas"

Scenario: Inserir Cartao com validade inválido
    Given o usuário está na página "http://localhost:3000/paymentMethod"
    When o usuário clica no botão "insert_payment"
    And o usuário clica no botão "select_cartao"
    And o usuário preenche o campo "inserir_nome_cartao" com "MasterCard", o campo "inserir_numero_cartao" com "8394204850258390", o campo "inserir_cvv" com "437", o campo "inserir_cpf_cartao" com "111.111.111-11", o campo "inserir_validade" com "2024-03-07" e clica no botão "inserir_cartao_botao"
    Then o usuário visualiza a mensagem "Informações inválidas"


