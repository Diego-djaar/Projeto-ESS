Feature: Estatisca de pedidos no mes
    As a Usuario
    I want to Ver as estatisticas de pedidos feitos por mim durante algum mes
    So that Eu posso fazer uma analise das minhas compras

Scenario: Estatísticas de pedidos não encontradas
    Given O usuário está logado na aplicação.
    When O usuário seleciona o mês de janeiro de 2023 para visualizar as estatísticas de pedidos.
    And O usuário não realizou nenhum pedido em janeiro de 2023.
    Then O sistema deve exibir uma mensagem de erro