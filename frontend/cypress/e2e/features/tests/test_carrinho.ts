import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

Given('o usuário está na página {string}', (page: string)=>{
    cy.visit(`http://localhost:3000/${page}`)
});

Given('o item de ID {string} está na lista de itens do carrinho', (string: string) => {
    const CPF = "123.456.789-10";

    cy.get('_inputCpf_1s4nr_33').type(CPF);

    cy.get('_viewCartButton_1s4nr_49').click();

    // Verificar se o item com o ID específico está presente na lista
    cy.get('_itemList_1s4nr_109')
      .find('_itemId_8sqz1_129')
      .contains(`(ID: ${string})`)
      .should('exist');
});

When('o usuário clica no botão {string} do item {string}', (string: string, string2: string) => {
    if (string === "Remover") {
        cy.get(`_itemList_1s4nr_109 li`).contains(`(ID: ${string2})`)
        .parents('li')
        .within(() => {
            // Dentro deste item, clique no botão com o texto específico.
            cy.get(`_itemRemove_1af1z_1`).click();
        });
    };
});

Then('o usuário não deve ver mais o item de ID {string} na lista de itens do carrinho', (string: string) => {
    const CPF = "123.456.789-10";

    // Verificar se o item com o ID específico está presente na lista
    cy.get('_itemList_1s4nr_109')
      .find('_itemId_8sqz1_129')
      .contains(`(ID: ${string})`)
      .should('not.exist')
});