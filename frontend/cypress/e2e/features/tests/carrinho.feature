Feature: Visualizar e modificar carrinho
    As um usuário
    I want to visualizar e modificar o conteúdo do meu carrinho
    So that eu possa decidir o que vou comprar


    Scenario: Remover item de carrinho com sucesso
        Given o usuário está na página "carrinho"
        And o item de ID "12345678" está na lista de itens do carrinho
        When o usuário clica no botão "remover" do item "12345678"
        Then o usuário não deve ver mais o item de ID "12345678" na lista de itens do carrinho

    Scenario: Alterar endereço com sucesso
        Given o usuário está na página "carrinho"
        And o endereço não foi registrado
        When o usuário clica no botão de "Alterar Endereço"
        And preenche todos os campos obrigatórios
        And o usuário clica no botão de "Salvar Endereço"
        Then o usuário visualiza um pop-up com o texto "Endereço alterado com sucesso!"


    Scenario: Alterar endereço com falha
        Given o usuário está na página "carrinho"
        And o endereço não foi registrado
        When o usuário clica no botão de "Alterar Endereço"
        And não preenche nenhum campo obrigatório
        And o usuário clica no botão de "Salvar Endereço"
        Then o usuário visualiza uma mensagem com o texto "Por favor, preencha todos os campos obrigatórios."

    Scenario: Incrementar item no carrinho com sucesso
        Given o usuário está na página "carrinho"
        And o usuário observa "1" na quantidade do item de ID "12345678"
        When o usuário clica no botão "+"
        Then o usuário observa "2" na quantidade do item de ID "12345678"

    Scenario: Decrementar item no carrinho com sucesso
        Given o usuário está na página "carrinho"
        And o usuário observa "2" na quantidade do item de ID "12345678"
        When o usuário clica no botão "-"
        Then o usuário observa "1" na quantidade do item de ID "12345678"

    Scenario: Decrementar item no carrinho quando quantidade é 1 com sucesso
        Given o usuário está na página "carrinho"
        And o usuário observa "1" na quantidade do item de ID "12345678"
        When o usuário clica no botão "-"
        Then o usuário não deve ver mais o item de ID "12345678" na lista de itens do carrinho