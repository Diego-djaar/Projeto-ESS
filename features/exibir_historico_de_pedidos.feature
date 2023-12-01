Feature: Exibir historico de pedidos
    As Usuario
    I want to Exibir meu histórico de pedidos feitos em um certo mes
    So that Eu posso ver minhas compras passadas

Scenario: Historico de pedidos nao encontrado
    Given O usuário está logado na aplicação.
    When o usuário seleciona uma data de início e uma data de término que não incluem nenhum pedido realizado pelo usuário.
    Then o sistema deve exibir uma mensagem de erro informando que nenhum pedido foi encontrado.