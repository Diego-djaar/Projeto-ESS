Feature: Exibir historico de pedidos
    As Usuario
    I want to Exibir meu histórico de pedidos feitos em um certo mes
    So that Eu posso ver minhas compras passadas

Scenario: Historico de pedidos nao encontrado
    Given O usuário está logado na aplicação
    When o usuário seleciona uma data de início e uma data de término que não incluem nenhum pedido realizado pelo usuário
    Then o sistema deve exibir uma mensagem de erro informando que nenhum pedido foi encontrado

Scenario: Exibir historico de pedidos
    Given O usuário está logado na aplicação
    When O usuário seleciona uma data de início e uma data de término para visualizar o histórico de pedidos
    Then O sistema deve exibir uma lista de todos os pedidos realizados pelo usuário dentro das datas selecionadas