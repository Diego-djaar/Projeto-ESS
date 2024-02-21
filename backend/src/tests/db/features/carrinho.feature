Feature: Carrinho database

Scenario: Criar carrinho
    When é criado um novo carrinho com os dados (CPF="123.456.789-10")
    Then a criação do carrinho é bem sucedida
    And o carrinho possui os dados (CPF="123.456.789-10", items={}, total="0.00", endereço=None)

Scenario: Adicionar item ao carrinho
    Given um carrinho de CPF "123.456.789-10" já foi criado
    When adiciona-se um item de id "12345678" ao carrinho
    Then o carrinho possui o item de id "12345678"