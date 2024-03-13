import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";
import { GetLogin } from "../../../../src/Services/login";
import { page_atual, set_page } from "../../../../src/Services/page_select";
import { login_request, remove_request, signup_request } from "../../../support/requests";

let fixture_campos = []
const fixture_senha = "Xyzw3456" // Senha padrão dos testes

// Scenario: Cadastro de usuário mal sucedido

// Given Eu não estou logado
Given("Eu não estou logado", () => {
    assert(!GetLogin());
});

// Given Eu estou na página de "signup”
Given("Eu estou na página de {string}", (page: string) => { 
    cy.visit('http://localhost:3123/'+page)
    set_page(page);
});

function write_signup_req(Nome: string, Sobrenome: string, Username: string, CPF: string,
    Address: string, CEP: string, Date: string, Email: string, Senha: string) {
    assert(page_atual == "signup");
    if (Nome !== "") {
        cy.get('input[id="Nome"]').type(Nome);
    }
    if (Sobrenome !== "") {
    cy.get("#Sobrenome").type(Sobrenome);
    }
    if (Username !== "") {
    cy.get("#Username").type(Username);
    }
    if (CPF !== "") {
    cy.get("#CPF").type(CPF);
    }
    if (Address !== "") {
    cy.get("#Endereço").type(Address);
    }
    if (CEP !== "") {
    cy.get("#CEP").type(CEP);
    }
    if (Date !== "") {
    cy.get("#Data_de_nascimento").type(Date);
    }
    if (Email !== "") {
    cy.get("#Email").type(Email);
    }
    if (Senha !== "") {
    cy.get("#Senha").type(Senha);
    }
    if (Senha !== "") {
    cy.get("#Repetir_Senha").type(Senha);
    }
}

// When Eu preencho os dados: nome: "Enzo Gabriel", sobrenome: "Rocha", user: "Enzo", CPF: 010.010.010-23,
// endereço: "Av. Dois Rios, 74 - Ibura, Recife - PE nº 700", CEP: "51230-000", data de nascimento: "02/02/2002",
// email: "EnzoGab@cin.ufpe.br", senha: "Xyzw3456"
When("Eu preencho os dados: nome: {string}, sobrenome: {string}, user: {string}, CPF: {string}, endereço: {string}, CEP: {string}, data de nascimento: {string}, email: {string}, senha: {string}",
    (Nome: string, Sobrenome: string, Username: string, CPF: string,
        Address: string, CEP: string, Date: string, Email: string, Senha: string) => {
    write_signup_req(Nome, Sobrenome,Username, CPF, Address, CEP, Date, Email, Senha)
});

// When Eu preencho os dados: nome: "Gabriel", Sobrenome: "Silva", User: "Gab", data de nascimento: 01-01-2001,
// email: "Gabriel@cin.ufpe.br", senha: "Abcd9678"
When("Eu preencho os dados: nome: {string}, Sobrenome: {string}, User: {string}, data de nascimento: {string}, email: {string}, senha: {string}",
    (Nome: string, Sobrenome: string, Username: string, Date: string, Email: string, Senha: string) => {
    write_signup_req(Nome, Sobrenome,Username, "", "", "", Date, Email, Senha)
    });

When("Eu preencho no campo {string} {string}", (campo: string, valor: string) => {
    cy.get("#" + campo).clear().type(valor);
    fixture_campos = [campo]
});

// When Eu deixo o campo "Email" em branco
When("Eu deixo o campo {string} em branco", (campo: string) => { 
    cy.get("#" + campo).clear();
    fixture_campos = [campo]
});

// When eu clico em "Cadastrar"
When("eu clico em {string}", (campo: string) => {
    cy.get("#" + campo).click();
});

// Then O cadastro não é bem sucedido
Then("O cadastro não é bem sucedido", () => {
    assert(page_atual==="signup")
});

// Then Eu sou notificado dos campos de cadastro que estão mal preenchidos
Then("Eu sou notificado dos campos de cadastro que estão mal preenchidos", () => {
    fixture_campos.forEach((campo)=>{
        cy.get("#"+campo).should('have.css', 'border-color', 'rgb(235, 27, 27)')
    });
});

// Scenario: Cadastro de usuário já existente
// Given Usuário "Enzo" está cadastrado, com os dados: nome: "Enzo Gabriel", sobrenome: "Rocha",
// user: "Enzo", CPF: "111.111.111-11, endereço: "Av.Dois Rios, 74 - Ibura, Recife - PE nº 700",
// CEP: "51230-000", data de nascimento: "2002-02-02", email: "EnzoGab @cin.ufpe.br", senha: "Xyzw3456"
Given("Usuário {string} está cadastrado, com os dados: nome: {string}, sobrenome: {string}, user: {string}, CPF: {string}, endereço: {string}, CEP: {string}, data de nascimento: {string}, email: {string}, senha: {string}",
    (_user: string, Nome: string, Sobrenome: string, Username: string, CPF: string,
        Address: string, CEP: string, Date: string, Email: string, Senha: string) => {
        
        login_request({
            "cpf_ou_user_ou_email": Username,
            "senha": Senha,
        }).then((r)=>{if (r.status === 200) {
            remove_request({"token": r.body.data.token })
        }})
        
        
        signup_request({
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
    });

// Then Eu sou notificado que o usuário "Enzo" já existe
Then("Eu sou notificado que o usuário {string} já existe", () => {
    cy.on('window:alert',(t)=>{
         //assertions
         assert(t.includes("Já existe uma conta com esse USER"));
      })
});

Then("Eu sou notificado que o usuário com esse {string} já existe", (campo: string) => {
    cy.on('window:alert',(t)=>{
         //assertions
         assert(t.includes(`Já existe uma conta com esse ${campo}`));
      })
});

Then("Eu sou redirecionado para a página de {string}", (page: string) => {
    cy.url().should('eq', `http://localhost:3123/${page}`);
});

Given("Usuário {string} não está cadastrado", (user: string) => {
        login_request({
            "cpf_ou_user_ou_email": user,
            "senha": fixture_senha,
        }).then((r)=>{if (r.status === 200) {
            remove_request({"token": r.body.data.token })
        }})
});

Then("O cadastro é bem sucedido", () => {
    cy.wait(2000) // necessário para carregar a página
})

Then("Estou logado como usuário {string}", (user: string) => {
    cy.get("#Username").should('have.text', `Username: ${user}`)
});