import axios, { AxiosError } from "axios";
import { set_page } from "./page_select";

let logado: boolean = false
let session_token = ""

export function SetToken(valor: string) {
    session_token = valor
    window.localStorage.setItem("session_token", session_token)
}

export function GetToken() {
    return window.localStorage.getItem("session_token")
}

export function GetLogin() {
    return JSON.parse(window.localStorage.getItem("logado")!)
}

export function SetLogin(valor: boolean) {
    logado = valor
    window.localStorage.setItem("logado", JSON.stringify(logado))
}

export function unlogin() {
    SetToken("")
    SetLogin(false)
}

// eslint-disable-next-line prefer-const
let login_input_functions = {}

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export function add_function(id: string, method: (arg1: string) => void) {
    login_input_functions[id] = method
    //console.log(signup_input_functions)
}

// eslint-disable-next-line @typescript-eslint/no-unused-vars
function ClearInputs() {
    Object.keys(LoginForm).forEach(loc => {
        // console.log(loc.toLowerCase()+"Color")
        login_input_functions[loc.toLowerCase() + "Color"]('normal')
    });
}

// eslint-disable-next-line prefer-const
let LoginForm = {
    "cpf_ou_user_ou_email": null,
    "senha": null
}

export function Init() {
    console.log(login_input_functions)
    Object.keys(LoginForm).forEach(loc => {
        //console.log(loc.toLowerCase() + "Text")
        //console.log(signup_input_functions[loc.toLowerCase() + "Text"])
        //console.log(SignUpForm[loc])
        console.log(loc.toLowerCase() + "Text")
        console.log(login_input_functions[loc.toLowerCase() + "Text"])

        login_input_functions[loc.toLowerCase() + "Text"](LoginForm[loc])
    });
}

export function CreateRequest(entry: string, value: string) {
    if (value === "") {
            LoginForm[entry.toLowerCase()] = null
        }
    LoginForm[entry.toLowerCase()] = value
    return true
}

export async function MakeRequest() {
    const val = await axios
        .post("http://127.0.0.1:8000/backend/api/auth/user/login", LoginForm)
        .then(function (response) {
            if (response?.status === 200) {
                if (response.data.message === "Login com sucesso") {
                    SetLogin(true)
                    SetToken(response.data.data.token)
                    console.log("session token: ",session_token)
                    set_page("User")
                }
            }
        })
        .catch(function (error: AxiosError) {
            if (axios.isAxiosError(error)) {
                if (error.response?.status === 401) {
                    const response = error.response;
                    alert(response.data.message)
                }
                if (error.response?.status === 422) {
                    alert("Dados incorretos")
                }
            }
            else {
                console.log("other error")
                console.log(error)
            }
        });
    return val
}