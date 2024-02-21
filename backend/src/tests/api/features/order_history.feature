Feature: Historico de Pedidos

  Scenario: Obter pedidos por CPF
    Given o OrdersService retorna uma lista de pedidos que contém os pedidos de ids "1" e "2"
    When uma requisição GET é enviada para "/Orders/orders_by_user/111.222.333-44"
    Then o status de resposta JSON deve ser "200"
    And  o JSON de resposta deve ser uma lista de pedidos
    And o pedido de id "1" e nome "Produto A" está na lista
    And o pedido de id "2" e nome "Produto B" está na lista

  Scenario: Usuário quer visualizar um pedido específico
    Given a lista de pedidos possui a chave CPF "111.222.333-44" e possui o pedido de ID "1" associado a ele
    When é solicitado uma requisição GET para "/Orders/order_from_user/" com o parâmetro CPF do usuário "111.222.333-44" e ID de pedido "1" 
    Then o status de resposta JSON deve ser "200"
    And a mensagem de resposta será "Pedido obtido com sucesso"
    And o JSON de resposta terá os dados do pedido "1"

   Scenario: Obter pedidos com determinado Filtro
     Given o OrdersService retorna uma lista de pedidos filtrados que contém o pedido de id "1"
     When uma requisição POST é enviada para "/Orders/orders_filtered/" com o body contendo o CPF "111.222.333-44", o price_max "20" e o restante dos campos nulos
     Then o status de resposta JSON deve ser "200"
     And  o JSON de resposta deve ser uma lista com um único pedido
     And o pedido de id "1" e nome "Produto A" está na lista