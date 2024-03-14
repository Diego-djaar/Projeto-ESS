Feature: Cálculo estimado de entrega

    Scenario: CEP do usuário que solicita a estimativa de entrega é inválido
    Given o usuário de CPF "331.704.260-52" e CEP "01001002" está cadastrado no sistema
    And o usuário está interessado em calcular a estimativa de entrega do produto de ID "1" e CEP "53010120"
    When uma requisição "GET" for enviada para "calcular tempo de entrega", com dados CPF "331.704.260-52" e ID do produto "1"
    Then o status de resposta deverá ser de "400"
    And o campo mensagem contém "CEP do usuário inválido!"

    Scenario: Estimativa de entrega bem sucedida para o mesmo estado
    Given o usuário de CPF "331.704.260-52" e CEP "50670901" está cadastrado no sistema
    And o usuário está interessado em calcular a estimativa de entrega do produto de ID "1" e CEP "53010120"
    When uma requisição "GET" for enviada para "calcular tempo de entrega", com dados CPF "331.704.260-52" e ID do produto "1"
    Then o status de resposta deverá ser de "200"
    And o campo mensagem contém "CEP do usuário inválido!"
    And o campo de dados terá data de pedido "19-02-2024", data de entrega "24-02-2024" e modelo de entrega "Entrega tradicional"

    Scenario: Estimativa de entrega bem sucedida para estados diferentes
    Given o usuário de CPF "331.704.260-52" e CEP "57690-000" está cadastrado no sistema
    And o usuário está interessado em calcular a estimativa de entrega do produto de ID "1" e CEP "53010120"
    When uma requisição "GET" for enviada para "calcular tempo de entrega", com dados CPF "331.704.260-52" e ID do produto "1"
    Then o status de resposta deverá ser de "200"
    And o campo mensagem contém "CEP do usuário inválido!"
    And o campo de dados terá data de pedido "19-02-2024", data de entrega "26-02-2024" e modelo de entrega "Entrega expressa"

    Scenario: Estimativa de entrega bem sucedida para regiões diferentes
    Given o usuário de CPF "331.704.260-52" e CEP "04109-130" está cadastrado no sistema
    And o usuário está interessado em calcular a estimativa de entrega do produto de ID "1" e CEP "53010120"
    When uma requisição "GET" for enviada para "calcular tempo de entrega", com dados CPF "331.704.260-52" e ID do produto "1"
    Then o status de resposta deverá ser de "200"
    And o campo mensagem contém "CEP do usuário inválido!"
    And o campo de dados terá data de pedido "19-02-2024", data de entrega "29-02-2024" e modelo de entrega "Entrega aérea"