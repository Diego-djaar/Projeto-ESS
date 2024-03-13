Feature: Cancelamento de pedidos

    Scenario: Cancelar pedido com sucesso
    Given o usuário de CPF "111.222.333-44" possui o produto de ID "1" e de status "On the way" atrelado a ele
    When é solicitado uma requisição "PUT" para cancelar pedido com dados ID do produto "1", CPF do usuário "111.222.333-44" e razão do cancelamento "Demorou muito"
    Then o status de resposta deverá ser de "200"
    And a mensagem de resposta deverá conter o produto foi cancelado com sucesso

    Scenario: Cancelar pedido já entregue mal sucedido
    Given o usuário de CPF "222.333.444-55" possui o produto de ID "3" e de status "Delivered" atrelado a ele
    When é solicitado uma requisição "PUT" para cancelar pedido com dados ID do produto "3", CPF do usuário "222.333.444-55" e razão do cancelamento "Demorou muito"
    Then o status de resposta deverá ser de "400"
    And a mensagem de resposta deverá conter que o produto já foi entregue

    Scenario: Cancelar pedido já cancelado mal sucedido
    Given o usuário de CPF "111.222.333-44" possui o produto de ID "2" e de status "Canceled" atrelado a ele
    When é solicitado uma requisição "PUT" para cancelar pedido com dados ID do produto "2", CPF do usuário "111.222.333-44" e razão do cancelamento "Demorou muito"
    Then o status de resposta deverá ser de "400"
    And a mensagem de resposta deverá conter que o produto já foi cancelado

    Scenario: Solicitação de todos os pedidos
    Given o usuário de CPF "331.704.260-52" possui os produtos de ID "1", "2" e "5" atrelados a ele e respectivamente status "Cancelado", "À caminho" e "Cancelado"
    When é solicitado uma requisição "POST" para "obter todos os pedidos cancelados" com o dado CPF do usuário "331.704.260-52" 
    Then o status de resposta deverá ser de "200"
    And a mensagem de resposta deverá conter "Os pedidos foram obtidos com sucesso!"
    And os dados da resposta devem conter as informações dos pedidos de ID "1" e "5"