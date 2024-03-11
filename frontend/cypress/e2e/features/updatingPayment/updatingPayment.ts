import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

Given("o usuário está na página {string}", (page: string) => {

    cy.visit(page); 

})

When("o usuário clica no botão {string}", (button: string) => {

    cy.getDataCy(button).click();

})

When("o usuário preenche o campo {string} com {string}, o campo {string} com {string} e clica no botão {string}", 
(campo1: string, nome: string, campo2: string, cpf: string, button: string) => {

    cy.getDataCy(campo1).type(nome);
    cy.getDataCy(campo2).type(cpf);
    cy.getDataCy(button).click();

})

When("o usuário preenche o campo {string} com {string}, o campo {string} com {string}, o campo {string} com {string}, o campo {string} com {string}, o campo {string} com {string} e clica no botão {string}", 
(nome_cartao_campo: string, nome_cartao: string, numero_cartao_campo: string, numero_cartao: string, cvv_campo: string, cvv: string, cpf_campo: string, cpf: string, validade_campo: string, validade: string, button: string) => {

    cy.getDataCy(nome_cartao_campo).type(nome_cartao);
    cy.getDataCy(numero_cartao_campo).type(numero_cartao);
    cy.getDataCy(cvv_campo).type(cvv);
    cy.getDataCy(cpf_campo).type(cpf);
    cy.getDataCy(validade_campo).type(validade);
    cy.getDataCy(button).click();

 })

Then("o usuário visualiza a mensagem {string}", (text: string) => {

    cy.on("window:alert", (str) => {
        expect(text).to.equal(str);
      });

})

Then("o usuário é direcionando para a página {string}", (page: string) => {

    cy.visit(page); 

})


