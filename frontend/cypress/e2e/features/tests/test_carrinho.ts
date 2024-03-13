import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

beforeEach(() => {
    // Chamada para a função/API que limpa a base de dados
    cy.request('DELETE', 'http://127.0.0.1:8000/backend/api/carrinho/clear_carts');
  });  

// Given('o usuário está na página {string}', (page: string)=>{
//     cy.visit(`http://localhost:3123/${page}`)
// });

Given('o item de ID {string} está na lista de itens do carrinho', (string: string) => {
    const CPF = "123.456.789-10";

    cy.get('input.inputCpf').type(CPF);

    cy.get('button.viewCartButton').click();

    cy.get('.itemPageButton').click();

    cy.get('.itemAddButton').click();

    cy.get('.cartButton').click();

    cy.get('button.viewCartButton').click();

    // Verificar se o item com o ID específico está presente na lista
    cy.get('.itemList > li').each(($li) => { 
        cy.wrap($li).find('span.itemID').contains(`(ID: ${string})`).should('exist');
    });
});

When('o usuário clica no botão {string} do item {string}', (string: string, string2: string) => {
    if (string === "remover") {
        cy.get('.itemList > li').each(($li) => {
            cy.wrap($li).find('span.itemID').contains(`(ID: ${string2})`).then(($span) => {
                // Verifica se o span contendo o ID do item foi encontrado
                if ($span) {
                    // Se o span com o ID do item existe, procura pelo botão de remover no mesmo 'li' e clica nele
                    cy.wrap($li).find('button.removeButton').click();
                }
            });
        });
    }
});

Then('o usuário não deve ver mais o item de ID {string} na lista de itens do carrinho', (itemID) => {
    const CPF = "123.456.789-10";

    cy.get('button.viewCartButton').click();

    // Carrinho vazio
    cy.get('.itemList').find('li').should('not.exist')
});

Given('o endereço não foi registrado', ()=> {
    const CPF = "123.456.789-10";

    cy.get('input.inputCpf').type(CPF);

    cy.get('button.viewCartButton').click();

    cy.get('.addressInfo').should('contain', 'Endereço não registrado');
});

When('o usuário clica no botão de {string}', (string: string) => {
    if (string === "Alterar Endereço") {
        cy.get('.modelButton').click();
    } else if (string === "Salvar Endereço") {
        cy.get('.saveButton').click();
    } else if (string === "+") {
        cy.get(".quantityPlus").click();
    } else if (string === "-") {
        cy.get(".quantityMinus").click();
    } else if (string === "Visualizar carrinho") {
        cy.get('button.viewCartButton').click();
    }
});

When('preenche todos os campos obrigatórios', ()=> {
    // O exemplo abaixo presume que você está dentro de um contexto 'it' ou 'beforeEach' do Cypress
    cy.fixture('address.json').then((address) => {
    Object.keys(address).forEach((key) => {
      cy.get(`input[name=${key}]`).type(address[key]);
        });
    });
  
});

Then('o usuário visualiza um pop-up com o texto {string}', (string: string) => {
    cy.get(".confirmationPopup").should('exist')
});

When('não preenche nenhum campo obrigatório', ()=>{

});

Then('o usuário visualiza uma mensagem com o texto {string}', (string: string)=>{
    cy.get('.errorMessage').should('exist');
    cy.get('.errorMessage').should('contain', string)
});

Given('o usuário observa {string} na quantidade do item de ID {string}', (string: string, string2: string) => {
    const CPF = '123.456.789-10'

    cy.get('input.inputCpf').type(CPF);

    cy.get('button.viewCartButton').click();

    cy.get('.itemPageButton').click();
    let quantidade: number = parseInt(string);
    for (let i = 0; i < quantidade; i++) { cy.get('.itemAddButton').click(); }

    cy.get('.cartButton').click();

    cy.get('button.viewCartButton').click();

    cy.get(".quantityValue").should('contain', string)
});

Then('o usuário vê {string} na quantidade do item de ID {string}', (string: string, string2: string) => {
    cy.get('.itemList > li').each(($li) => {
        cy.wrap($li).find('span.itemID').contains(`(ID: ${string2})`).then(($li) => {
            cy.get(".quantityValue").should('contain', string)
        })});
});

// Integração
Then('o carrinho de CPF {string} é criado', (string: string) => {
    cy.request('GET', `http://127.0.0.1:8000/backend/api/carrinho/view/${string}`)
});

When('o usuário coloca o CPF {string} no campo de visualizar carrinho', (string: string) => {
    cy.get('input.inputCpf').type(string);
});

Then('o usuário vê um carrinho vazio', () => {
    cy.get('.itemList').find('li').should('not.exist')
});