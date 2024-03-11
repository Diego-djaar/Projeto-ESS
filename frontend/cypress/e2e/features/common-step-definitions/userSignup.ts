import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";
import { logado } from "../../../../src/Services/login";
import { page_atual, set_page } from "../../../../src/Services/page_select";
import { post } from "../../../../src/Services/sync_req"

function post(body, fail = false) {
    return cy.request({ method: 'POST', url: "http://127.0.0.1:8000/backend/api/auth/user/register", body:body, failOnStatusCode: fail})
}

// Scenario: Cadastro de usuário mal sucedido

// Given Eu não estou logado
Given("Eu não estou logado", () => {
    assert(!logado);
});

// Given Eu estou na página de "signup”
Given("Eu estou na página de {string}", (page: string) => { 
    cy.visit('http://localhost:3123')
    set_page(page);
});

// When Eu preencho os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: 010.010.010-23,
// endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "02/02/2002",
// email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456"
When("Eu preencho os dados: nome: {string}, sobrenome: {string}, user: {string}, CPF: {string}, endereço: {string}, CEP: {string}, data de nascimento: {string}, email: {string}, senha: {string}",
    (Nome: string, Sobrenome: string, Username: string, CPF: string,
        Address: string, CEP: string, Date: string, Email: string, Senha: string) => {
    assert(page_atual == "signup");
    cy.get('input[id="Nome"]').type(Nome);
    cy.get("#Sobrenome").type(Sobrenome);
    cy.get("#Username").type(Username);
    cy.get("#CPF").type(CPF);
    cy.get("#Endereço").type(Address);
    cy.get("#CEP").type(CEP);
    cy.get("#Data_de_nascimento").type(Date);
    cy.get("#Email").type(Email);
    cy.get("#Senha").type(Senha);
    cy.get("#Repetir_Senha").type(Senha);
});

// When Eu deixo o campo "Email" em branco
When("Eu deixo o campo {string} em branco", (campo: string) => { 
    cy.get("#" + campo).clear();
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

// Scenario: Cadastro de usuário já existente
// Given Usuário "Enzo" está cadastrado, com os dados: nome: "Enzo Gabriel", sobrenome: "Rocha",
// user: "Enzo", CPF: "111.111.111-11, endereço: "Av.Dois Rios, 74 - Ibura, Recife - PE nº 700",
// CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab @cin.ufpe.br", senha: "Xyzw3456"
Given("Usuário {string} está cadastrado, com os dados: nome: {string}, sobrenome: {string}, user: {string}, CPF: {string}, endereço: {string}, CEP: {string}, data de nascimento: {string}, email: {string}, senha: {string}",
    (_user: string, Nome: string, Sobrenome: string, Username: string, CPF: string,
        Address: string, CEP: string, Date: string, Email: string, Senha: string) => {
        const xhr = post({
            "username": Username,
            "nome": Nome,
            "sobrenome": Sobrenome,
            "cpf": CPF,
            "data_de_nascimento": Date,
            "email": Email,
            "senha": Senha,
            "endereço": Address,
            "CEP": CEP
        })
        cy.log(xhr)
    });

// Then Eu sou notificado que o usuário "Enzo" já existe
Then("Eu sou notificado que o usuário {string} já existe", () => {
    expect(cy.stub().getCall(0))
});