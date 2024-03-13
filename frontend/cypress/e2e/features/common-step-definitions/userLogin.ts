// eslint-disable-next-line @typescript-eslint/no-unused-vars
import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";
import { GetLogin } from "../../../../src/Services/login";

Then("o login é bem sucedido", function () {
    cy.wait(2000) // esperar carregar página
});

Then("Eu visualizo a mensagem {string}", (message: string) => {
    cy.on('window:alert',(t)=>{
         //assertions
         assert(t===message);
      })
});

Then("permanece na página {string}", (page: string) => {
    cy.url().should('eq', `http://localhost:3123/${page}`);
});