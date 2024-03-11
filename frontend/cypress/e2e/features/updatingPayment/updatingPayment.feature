# Feature: Atualizando métodos de pagamento
#     As a usuário 
#     I want atualizar as informações dos métodos de pagamento cadastrados
#     so that eu posso ter métodos de pagamento com informações atualizadas em meu perfil

# Scenario: atualizando pix 
#     Given o usuário está na página "http://localhost:3000/paymentMethod"
#     When o usuário clica no botão "update_payment"
#     And o usuário clica no botão "select_update_pix"
#     And o usuário cujo pix de nome "Breno Gabriel de Melo Lima" e cpf "333.333.333-33" preenche o campo "update_id_pix" com o id do método, o campo "update_nome_pix" com "Mariano Alvez da Costa" e clica no botão "update_pix_botao"
#     Then o usuário visualiza a mensagem "Dados atualizados com sucesso"
#     And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/updating"

# Scenario: atualizando boleto 
#     Given o usuário está na página "http://localhost:3000/paymentMethod"
#     When o usuário clica no botão "update_payment"
#     And o usuário clica no botão "select_update_boleto"
#     And o usuário cujo pix de nome "Breno Gabriel de Melo Lima" e cpf "333.333.333-33" preenche o campo "update_id_boleto" com o id do método, o campo "update_nome_boleto" com "Mariano Alvez da Costa" e clica no botão "update_boleto_botao"
#     Then o usuário visualiza a mensagem "Dados atualizados com sucesso"
#     And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/updating"

# Scenario: atualizando pix com ID incorreto 
#     Given o usuário está na página "http://localhost:3000/paymentMethod"
#     When o usuário clica no botão "update_payment"
#     And o usuário clica no botão "select_update_pix"
#     And o usuário preenche o campo "update_id_pix" com "0cc12576-0a25-429c-b12f-66d1d3c", o campo "update_nome_pix" com "Breno Gabriel de Melo Lima" e clica no botão "update_pix_botao"
#     Then o usuário visualiza a mensagem "ID não encontrado na base de dados"
#     And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/updating"

# Scenario: atualizando boleto com ID incorreto 
#     Given o usuário está na página "http://localhost:3000/paymentMethod"
#     When o usuário clica no botão "update_payment"
#     And o usuário clica no botão "select_update_boleto"
#     And o usuário preenche o campo "update_id_boleto" com "2966b7ce-544f-45cb-8ba3-7f56cc8", o campo "update_nome_boleto" com "Breno Gabriel de Melo Lima" e clica no botão "update_pix_botao"
#     Then o usuário visualiza a mensagem "ID não encontrado na base de dados"
#     And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/updating"

# Scenario: atualizando cartão
#     Given o usuário está na página "http://localhost:3000/paymentMethod"
#     When o usuário clica no botão "update_payment"
#     And o usuário clica no botão "select_update_cartao"
#     And o usuário preenche o campo "update_id_cartao" com "0b0b343d-53ba-4cf7-b693-a9947f917bf0", o campo "update_nome_cartao" com "MasterCard", o campo "update_numero_cartao" com "4556193045897381", o campo "update_cvv_cartao" com "938", o campo "update_validade_cartao" com "2025-06-17" e clica no botão "update_cartao_botao"
#     Then o usuário visualiza a mensagem "Método de pagamento cadastrado com sucesso"
#     And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/updating"

# Scenario: atualizando cartão com ID incorreto
#     Given o usuário está na página "http://localhost:3000/paymentMethod"
#     When o usuário clica no botão "update_payment"
#     And o usuário clica no botão "select_update_cartao"
#     And o usuário preenche o campo "update_id_cartao" com "0b0b343d-53ba-4cf7-b693-a9947f91", o campo "update_nome_cartao" com "MasterCard", o campo "update_numero_cartao" com "4556193045897381", o campo "update_cvv_cartao" com "938", o campo "update_validade_cartao" com "2025-06-17" e clica no botão "update_cartao_botao"
#     Then o usuário visualiza a mensagem "Método de pagamento cadastrado com sucesso"
#     And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/updating"

# Scenario: atualizando cartão fora da validade
#     Given o usuário está na página "http://localhost:3000/paymentMethod"
#     When o usuário clica no botão "update_payment"
#     And o usuário clica no botão "select_update_cartao"
#     And o usuário preenche o campo "update_id_cartao" com "0b0b343d-53ba-4cf7-b693-a9947f917bf0", o campo "update_nome_cartao" com "Nubank", o campo "update_numero_cartao" com "4556193045897381", o campo "update_cvv_cartao" com "938", o campo "update_validade_cartao" com "2020-06-17" e clica no botão "update_cartao_botao"
#     Then o usuário visualiza a mensagem "Informações inválidas"
#     And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/updating"


# Scenario: atualizando cartão com número inválido 
#     Given o usuário está na página "http://localhost:3000/paymentMethod"
#     When o usuário clica no botão "update_payment"
#     And o usuário clica no botão "select_update_cartao"
#     And o usuário preenche o campo "update_id_cartao" com "0b0b343d-53ba-4cf7-b693-a9947f917bf0", o campo "update_nome_cartao" com "MasterCard", o campo "update_numero_cartao" com "455619304435", o campo "update_cvv_cartao" com "938", o campo "update_validade_cartao" com "2026-06-17" e clica no botão "update_cartao_botao"
#     Then o usuário visualiza a mensagem "Informações inválidas"
#     And o usuário é direcionando para a página "http://localhost:3000/paymentMethod/updating"