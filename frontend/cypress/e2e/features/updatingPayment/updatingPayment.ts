import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

Given("o usuário está na página {string}", (page: string) => {

    cy.visit(page); 

})

When("o usuário clica no botão {string}", (button: string) => {

    cy.getDataCy(button).click();

})

When("o usuário cujo pix de nome {string} e cpf {string} preenche o campo {string} com o id do método, o campo {string} com {string} e clica no botão {string}", 
(nome: string, cpf: string, campo_id: string, novo_nome_campo: string, novo_nome: string, button: string ) => {

    const body = {
        "nome_completo": nome, 
        "cpf": cpf 
    }

    cy.request("POST", "http://127.0.0.1:8000/backend/api/payment/inserting/pix", body).then((response) => {
            const id = response.body.data.ID;
            cy.getDataCy(campo_id).type(id);
            cy.getDataCy(novo_nome_campo).type(novo_nome);
            cy.getDataCy(button).click();
    });  

});

When("o usuário cujo boleto de nome {string} e cpf {string} preenche o campo {string} com o id do método, o campo {string} com {string} e clica no botão {string}", 
(nome: string, cpf: string, campo_id: string, novo_nome_campo: string, novo_nome: string, button: string ) => {

    const body = {
        "nome_completo": nome, 
        "cpf": cpf 
    }

    cy.request("POST", "http://127.0.0.1:8000/backend/api/payment/inserting/boleto", body).then((response) => {
            const id = response.body.data.ID;
            cy.getDataCy(campo_id).type(id);
            cy.getDataCy(novo_nome_campo).type(novo_nome);
            cy.getDataCy(button).click();
    // });  

});

When("o usuário preenche o campo {string} com {string}, o campo {string} com {string}, o campo {string} com {string}, o campo {string} com {string}, o campo {string} com {string} e clica no botão {string}", 
(nome_cartao_campo: string, nome_cartao: string, numero_cartao_campo: string, numero_cartao: string, cvv_campo: string, cvv: string, cpf_campo: string, cpf: string, validade_campo: string, validade: string, button: string) => {

    cy.getDataCy(nome_cartao_campo).type(nome_cartao);
    cy.getDataCy(numero_cartao_campo).type(numero_cartao);
    cy.getDataCy(cvv_campo).type(cvv);
    cy.getDataCy(cpf_campo).type(cpf);
    cy.getDataCy(validade_campo).type(validade);
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

      cy.wait(5000);

})

Then("o usuário é direcionando para a página {string}", (page: string) => {

    cy.visit(page); 

})