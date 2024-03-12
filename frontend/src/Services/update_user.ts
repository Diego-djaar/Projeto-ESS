import axios, { AxiosError } from "axios"
import { GetLogin, GetToken, SetLogin, SetToken, unlogin } from "./login"
import { set_page } from "./page_select"
import { GetUser, UserData } from "./user"


// eslint-disable-next-line prefer-const
let update_input_functions = {}

const fields = ['nome', 'sobrenome', 'data_de_nascimento', 'endereço', 'CEP']

export function CreateRequest(entry: string, value: string) {
    if (entry === "CEP") {
        form.new_data[entry] = value
        if (value === "") {
            form.new_data[entry] = null
        }
    }
    else {
        if (value === "") {
            form.new_data[entry.toLowerCase()] = null
        }
        form.new_data[entry.toLowerCase()] = value
    }
    console.log(form)
    return true;
}

let form = {
  "token": {
    "token": GetToken()
  },
  "new_data": {
    "username": null,
    "nome": null,
    "sobrenome": null,
    "cpf": null,
    "data_de_nascimento": null,
    "email": null,
    "endereço": null,
    "CEP": null
  }
}

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export function add_function(id: string, method: (arg1: string) => void) {
    update_input_functions[id] = method
}

export async function Init(func: () => void) {
    if (!GetLogin()) {
        set_page("login")
    }
    await GetUser(true)
    func()
    form.new_data = UserData
    
    console.log(update_input_functions)
    fields.forEach(loc => {
        console.log(form.new_data[loc])
        update_input_functions[loc.toLowerCase() + "Text"](form.new_data[loc])
    });
}

export async function MakeRequest() {
    const val = await axios
        .patch("http://127.0.0.1:8000/backend/api/auth/user/update", form)
        .then(function () {
            // Sucesso
            const token = GetToken()
            unlogin()
            SetLogin(true)
            SetToken(token!)
            GetUser(true)
            set_page("user")

            return
        }).catch(function () { alert("ocorreu um erro ao atualizar os dados")})
    return val;
}
