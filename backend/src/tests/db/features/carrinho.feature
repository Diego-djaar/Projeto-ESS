Feature: Carrinho database

Scenario: Criar carrinho
    When é criado um novo carrinho com os dados (CPF="123.456.789-10")
    Then a criação do carrinho é bem sucedida
    And o carrinho possui os dados (CPF="123.456.789-10", items={}, total="0.00", endereço=None)