// eslint-disable-next-line @typescript-eslint/no-unused-vars
import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";
import { login_request } from "../../../support/requests";
import { fixture_senha } from "./userSignup";


Then("Usuário {string} não está mais cadastrado", (user: string) => { 
    login_request({
            "cpf_ou_user_ou_email": user,
            "senha": fixture_senha,
        }).then((r)=>{assert(r.status===401)})
});

When("vejo no campo {string} {string}", (campo, valor) => {
    cy.get(`#${campo}`).should('have.text', valor)
});