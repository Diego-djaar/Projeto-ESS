import axios, { AxiosError } from "axios";
import { GetLogin, GetToken, SetLogin, SetToken } from "./login";
import { set_page } from "./page_select";

export let UserData = {
    "username": null,
    "nome": null,
    "sobrenome": null,
    "cpf": null,
    "data_de_nascimento": null,
    "email": null,
    "endereço": null,
    "CEP": null
}

export async function Init(func: () => void) {
    if (!GetLogin()) {
        set_page("login")
    }
    await GetUser(true)
    func()
}

async function GetUser(redirect = false) {
    const val = await axios
        .post('http://127.0.0.1:8000/backend/api/auth/user/verify', { "token": GetToken() })
        .then(function (response) { 
            if (response?.status === 200) { 
                UserData = response.data.data.user
                console.log(UserData)
                return
            }
        })
        .catch(function (error: AxiosError) { 
            if (axios.isAxiosError(error)) {
                if (error.response?.status === 401) { 
                    SetLogin(false)
                    SetToken("")
                    if (!redirect) {
                        set_page("login")
                    }
                }
            }
        })
    return val
}
