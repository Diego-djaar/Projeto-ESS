import Button from "../../Components/Button/button"
import { set_page } from "../../Services/page_select"
import "./update.css"
import Input from "../../Components/Input/inputs"
import { UserData } from "../../Services/user"
import { Component } from "react"
import { CreateRequest, Init, MakeRequest, add_function } from "../../Services/update_user"


class UpdateUser extends Component {
    state: {user_data: {"username": string,
                "nome": string,
                "sobrenome": string,
                "cpf": string,
                "data_de_nascimento": string,
                "email": string,
                "endereço": string,
                 "CEP": string
        }
    }
    
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
                <Button func={() => set_page("main")} text={"Back to main Page"} style={{}} id="Main"/>
                <h1 className="signup-text">Atualize os dados</h1>
                <div className="two-inputs">
                    <Input campo="Nome" type="Name" internal="div1" form={CreateRequest} add_function={add_function}  initial_text={ this.state.user_data.nome} />
                    <Input campo="Sobrenome" type="surname" internal="div1" form={CreateRequest} add_function={add_function}  initial_text={ this.state.user_data.sobrenome} />
                </div>
                <div className="two-inputs">
                    <Input campo="Data_de_nascimento" type="Date" internal="div1" form={CreateRequest} add_function={add_function}  initial_text={ this.state.user_data.data_de_nascimento}/>
                    <Input campo="Endereço" type="Address" internal="div1" form={CreateRequest} add_function={add_function} initial_text={ this.state.user_data.endereço} />
                </div>
                <div className="two-inputs">
                    <Input campo="CEP" type="CEP" internal="div1" form={CreateRequest} add_function={add_function}  initial_text={ this.state.user_data.CEP} />
                    <h1></h1>
                </div>
                <Button func={MakeRequest} text="update" style={{ color: "black", fontSize: "30px" }} id="UpdateUser"/>
            </div>
        )
        return val
    }
}

export default UpdateUser