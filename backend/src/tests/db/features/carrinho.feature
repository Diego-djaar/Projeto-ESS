Feature: Carrinho database

Scenario: Criar carrinho
    When é criado um novo carrinho com os dados (CPF="123.456.789-10")
    Then a criação do carrinho é bem sucedida
    And o carrinho possui os dados (CPF="123.456.789-10", items={}, total="0.00", endereço=None)

Scenario: Adicionar item ao carrinho
    Given um carrinho de CPF "123.456.789-10" já foi criado
    When adiciona-se um item de id "12345678" ao carrinho
    Then o carrinho possui o item de id "12345678"

Scenario: Remover item de carrinho
    Given um carrinho de CPF "123.456.789-10" já foi criado
    And o carrinho possui o item de id "12345678"
    When remove-se um item de id "12345678" do carrinho
    Then o carrinho está vazio

Scenario: Alterar endereço do carrinho
    Given um carrinho de CPF "123.456.789-10" já foi criado
    And o carrinho não possui endereço registrado
    When adiciona-se o endereço "Rua , 225, Bairro, Cidade, Estado, CEP, País, Complemento"
    Then o carrinho possui endereço "Rua , 225, Complemento\nBairro, Cidade - Estado\nCEP: CEP\nPaís"