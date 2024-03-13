import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";



// Given("o usuário está na página {string}", (page: string) => {

//     cy.visit(page); 

// })



When("o usuário clica no botão {string}", (button: string) => {

    cy.getDataCy(button).click();

})



When("o usuário cujo pix de nome {string} e cpf {string} preenche o campo {string} com o id do método e clica em {string}", 
(nome: string, cpf: string, id_campo: string, button: string) => {

    const body = {
        "nome_completo": nome, 
        "cpf": cpf 
    }

    cy.request("POST", "http://127.0.0.1:8000/backend/api/payment/inserting/pix", body).then((response) => {
            const id = response.body.data.ID;
            cy.getDataCy(id_campo).type(id);
            cy.getDataCy(button).click();
    });

})


When("o usuário cujo boleto de nome {string} e cpf {string} preenche o campo {string} com o id do método e clica em {string}", 
(nome: string, cpf: string, id_campo: string, button: string) => {

    const body = {
        "nome_completo": nome, 
        "cpf": cpf 
    }

    cy.request("POST", "http://127.0.0.1:8000/backend/api/payment/inserting/boleto", body).then((response) => {
            const id = response.body.data.ID;
            cy.getDataCy(id_campo).type(id);
            cy.getDataCy(button).click();
    });

})


When("o usuário cujo cartão de nome {string}, numero  {string}, cvv {string}, cpf {string}, validade {string} preenche o campo {string} com o id do método e clica em {string}", 
(nome: string, numero: string, cvv: string, cpf: string, validade: string, campo_id: string, delete_butoon: string) => {

    const body = {
        "nome_cartao": nome,
        "numero_cartao": numero,
        "cvv": cvv,
        "cpf": cpf,
        "validade": validade
      }

    cy.request("POST", "http://127.0.0.1:8000/backend/api/payment/inserting/cartao", body).then((response) => {
            const id = response.body.data.ID;
            cy.getDataCy(campo_id).type(id);
            cy.getDataCy(delete_butoon).click();
    });

})


When("o usuário preenche o campo {string} com o id incorreto do método e clica em {string}", (id_campo: string, button: string) => {

    cy.getDataCy(id_campo).type("29342909jfr3940r");
    cy.getDataCy(button).click();

})


// Then("o usuário visualiza a mensagem {string}", (text: string) => {
//     cy.on("window:alert", (str) => {
//       expect(text).to.equal(str);
//     });
  
//     cy.wait(1000);
//   });
  
  
Then("o usuário é direcionando para a página {string}", (page: string) => {

    cy.visit(page); 

})
