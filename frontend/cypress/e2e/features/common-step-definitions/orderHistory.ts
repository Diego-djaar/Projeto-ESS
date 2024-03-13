import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

// Scenario: Todos os pedidos
//Given: common-step-definitions.ts

Given("o usuário está na página {string}", (page: string) => {
    cy.visit(page);
});

When(
    "o usuario aperta no botão {string}",
    (button: string) => {
        cy.getDataCy(button).click();
    }
);

Then(
    "o usuario deve ver o pedido de id {string}",
    (orderId: string) => {
        cy.getDataCy(`[data-cy="${orderId}"]`).should("contain", orderId);
    }
)