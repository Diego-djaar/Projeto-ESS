import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";
import { logado } from "../../Services/login";
import { set_page } from "../../Services/page_select";
// Scenario: Cadastro de usuário mal sucedido

// Given Eu não estou logado
Given("Eu não estou logado", () => {
    assert(!logado);
});

// Given Eu estou na página de "signup”
Given("Eu estou na página de {string}", (page: string) => { 
    set_page(page);
});

// When Eu preencho os dados: (nome: “Enzo Gabriel“, sobrenome: “Rocha“, user: “Enzo“, CPF: 010.010.010-23, endereço:  “Av. Dois Rios, 74 - Ibura, Recife - PE nº 700“, CEP: “51230-000“, data de nascimento: “02/02/2002“, email: “EnzoGab@cin.ufpe.br“, senha: “Xyzw3456“)
When("Eu preencho os dados: (nome: {string}, sobrenome: {string}, user: {string}, CPF: {string}, \
    endereço:  {string}, CEP: {string}, data de nascimento: {string}, \
    email: {string}, senha: {string})", (Nome: string, Sobrenome: string, Username: string, CPF: string,
    Address: string, CEP: string, Date: string, Email: string, Senha: string) => { 
    cy.get("#Nome").type(Nome);
    cy.get("#Sobrenome").type(Sobrenome);
    cy.get("#Username").type(Username);
    cy.get("#CPF").type(CPF);
    cy.get("#Address").type(Address);
    cy.get("#CEP").type(CEP);
    cy.get("#Date").type(Date);
    cy.get("#Email").type(Email);
    cy.get("#Senha").type(Senha);
    cy.get("#Repetir_Senha").type(Senha);
});

// When Eu deixo o campo "Email" em branco
When("Eu deixo o campo {string} em branco", (campo: string) => { 
    cy.get("#" + campo).type("");
});

// When eu clico em "Cadastrar"
When("eu clico em {string}", (campo: string) => {
    cy.get("#" + campo).click();
});

// Then O cadastro não é bem sucedido
Then("O cadastro não é bem sucedido", () => {
    // Nada acontece
});

// Then Eu sou notificado dos campos de cadastro que estão mal preenchidos
Then("Eu sou notificado dos campos de cadastro que estão mal preenchidos", () => {
    // Email fica vermelho
});