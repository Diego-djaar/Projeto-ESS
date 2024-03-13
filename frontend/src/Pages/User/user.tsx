import { Component } from "react"
import { Init, UserData } from "../../Services/user"
import Button from "../../Components/Button/button";
import { set_page } from "../../Services/page_select";
import { exclude, unlogin } from "../../Services/login";

export default class User extends Component{
    state: {user_data: {"username": string,
                "nome": string,
                "sobrenome": string,
                "cpf": string,
                "data_de_nascimento": string,
                "email": string,
                "endereço": string,
                "CEP": string}}
    constructor(props: Record<string, never>) {
        super(props);
        this.state = {
            user_data: {
                "username": "",
                "nome": "",
                "sobrenome": "",
                "cpf": "",
                "data_de_nascimento": "",
                "email": "",
                "endereço": "",
                "CEP": ""
            }
        }
        this.updateData = this.updateData.bind(this)
    }

    updateData() {
        this.setState({user_data: UserData})
    }

    async componentDidMount() {
        await Init(this.updateData)
    }

    render() {
        const val = (
            <div>
                <h1>Dados Usuário:</h1>
                <h2 id="Username">Username: { this.state.user_data.username}</h2>
                <h2>Nome: { this.state.user_data.nome}</h2>
                <h2 id="Sobrenome">Sobrenome: { this.state.user_data.sobrenome}</h2>
                <h2>CPF: { this.state.user_data.cpf}</h2>
                <h2>Data de nascimento: { this.state.user_data.data_de_nascimento}</h2>
                <h2>Email: { this.state.user_data.email}</h2>
                <h2>Endereço: { this.state.user_data.endereço}</h2>
                <h2>CEP: {this.state.user_data.CEP}</h2>
                <Button func={() => set_page("main")} text={"Página principal"} style={{}} id="Main" />
                <h1></h1>
                <Button func={() => { unlogin(); window.location.reload() }} text={"Sair"} style={{}} id="Unlogin"/>
                <h1></h1>
                <Button func={() => { exclude(); window.location.reload() }} text={"Excluir Usuário"} style={{}} id="Exclude"/>
                <h1></h1>
                <Button func={() => { set_page("update_user") }} text={"Atualizar Dados"} style={{}} id="Update"/>
            </div>
        )
        return val
    }
}