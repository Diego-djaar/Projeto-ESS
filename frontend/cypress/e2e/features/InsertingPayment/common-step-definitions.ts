import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

Given("o usuário está na página {string}", (page: string) => {

    cy.visit(page); 

})
