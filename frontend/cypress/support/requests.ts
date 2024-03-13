export function signup_request(body, fail = false) {
    return cy.request({ method: 'POST', url: "http://127.0.0.1:8000/backend/api/auth/user/register", body: body, failOnStatusCode: fail })

}

export function login_request(body, fail = false) {
    return cy.request({method: 'POST', url: "http://127.0.0.1:8000/backend/api/auth/user/login", body: body, failOnStatusCode: fail})

}

export function remove_request(body, fail = false) {
    return cy.request({method: 'DELETE', url: "http://127.0.0.1:8000/backend/api/auth/user/remove", body:body, failOnStatusCode: fail})

}