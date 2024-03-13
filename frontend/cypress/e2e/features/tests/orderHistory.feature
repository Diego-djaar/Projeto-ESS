Feature: Historico de Pedidos
    As a usuario
    I want visualizar os pedidos que já fiz
    so that possa ver os detalhes e filtrar

    Scenario: Todos os pedidos
        Given o usuário está na página "orderhistory"
        When o usuario aperta no botão "limpar"
        Then o usuario deve ver o pedido de id "1"

# Scenario: Pedidos Filtrados
# Given o usuario está na página "orderhistory"
# When o usuario preenche o campo "Preço Mínimo" com "800"
# When o usuario aperta no botão "pesquisar"
# Then o usuario deve ver o pedido de id "3"

# Scenario: Paginação
# Given o usuario está na página "orderhistory"
# When o usuario aperta no botão "next"
# Then o usuario deve ver o pedido de id "6"

    