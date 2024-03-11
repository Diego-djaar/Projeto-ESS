import axios, { AxiosError } from "axios"
import { GetBody, GetData, GetDetail } from "./request"
import { SetLogin } from "./login"

// eslint-disable-next-line prefer-const
let SignUpForm = {
  "username": null,
  "nome": null,
  "sobrenome": null,
  "cpf": null,
  "data_de_nascimento": null,
  "email": null,
  "senha": null,
  "endereço": null,
   "CEP": null,
  "repetir_senha": null,
}

// eslint-disable-next-line prefer-const
let signup_input_functions = {}
// eslint-disable-next-line @typescript-eslint/no-unused-vars
export function add_function(id: string, method: (arg1: string) => void) {
    signup_input_functions[id] = method
    //console.log(signup_input_functions)
}

function ClearInputs() {
    Object.keys(SignUpForm).forEach(loc => {
        // console.log(loc.toLowerCase()+"Color")
        signup_input_functions[loc.toLowerCase() + "Color"]('normal')
    });
}
export function Init() {
    console.log(signup_input_functions)
    Object.keys(SignUpForm).forEach(loc => {
        //console.log(loc.toLowerCase() + "Text")
        //console.log(signup_input_functions[loc.toLowerCase() + "Text"])
        //console.log(SignUpForm[loc])
        signup_input_functions[loc.toLowerCase() + "Text"](SignUpForm[loc])
    });
}

export function CreateRequest(entry: string, value: string) {
    
    if (entry === "CEP") {
        SignUpForm[entry] = value
        if (value === "") {
            SignUpForm[entry] = null
        }
    }
    else {
        if (value === "") {
            SignUpForm[entry.toLowerCase()] = null
        }
        SignUpForm[entry.toLowerCase()] = value
    }
    //console.log(JSON.stringify(SignUpForm))
    if (entry === "Repetir_Senha" && value !== SignUpForm.senha) {
        return false;
    }
    if (entry === "Senha") {
        if (value !== SignUpForm.repetir_senha) {
            signup_input_functions['repetir_senhaColor']('altered')
        } else {
            signup_input_functions['repetir_senhaColor']('normal')
        }
    }
    return true;
}

export async function MakeRequest() {
    if (SignUpForm.repetir_senha !== SignUpForm.senha) {
        return null;
    }
    console.log(SignUpForm)
    const val = await axios
    .post("http://127.0.0.1:8000/backend/api/auth/user/register", SignUpForm)
    .then(function (response) {
        console.log(response.data);
        if (response.data.message === "Usuário cadastrado com sucesso") {
            SetLogin(true)
            // Temporário
            alert('Cadastro realizado com sucesso')
        }
    })
    .catch(function (error: AxiosError) {
        if (axios.isAxiosError(error)) {
            if (error.response?.status == 422) {
                const response = error.response;
                // console.log(response)
                const data = GetBody(response)
                const detail = GetDetail(data)
                console.log(detail)
                const locations = detail.loc
                ClearInputs()
                locations.forEach(loc => {
                    console.log(signup_input_functions[loc + 'Color'])
                    if (loc != 'body') {
                        console.log(signup_input_functions[loc + "Color"])
                        signup_input_functions[loc + "Color"]('altered')
                    }
                });
            }
            else if (error.response?.status == 400) {
                const response = error.response;
                const data: string[] = GetData(response).data
                ClearInputs()
                if (data.includes("Campo CEP mal formulado")) {
                    signup_input_functions["cepColor"]('altered')
                }
                Object.keys(SignUpForm).forEach(key => {
                    if (data.includes("Campo " + key.toUpperCase() + " mal formulado")) {
                        signup_input_functions[key.toLowerCase() + "Color"]('altered')
                    }
                    
                });
                console.log(data)
            }
            else if (error.response?.status == 401) {
                console.log([error.response.data.message]);
                console.log(error.response.data.data);
                const res = [...[error.response.data.message], ...error.response.data.data];
                console.log(res.join(" "))
                alert(res)
            }
            console.log(error)
        }
        else {
            console.log("other error")
            console.log(error)
        }
    });
    console.log(val)
}