import Button from "../../Components/Button/button"
import { set_page } from "../../Services/page_select"
import "./signup.css"
import Input from "../../Components/Input/inputs"
import { CreateRequest, MakeRequest, add_function, Init } from "../../Services/sign_up"
import { Component } from "react"


class SignUp extends Component {

    componentDidMount() {
        Init();
    }

    render() {
        const val = (
            <div>
                <Button func={() => set_page("main")} text={"Back to main Page"} style={{}} id="Main"/>
                <h1 className="signup-text">Sign Up</h1>
                <div className="two-inputs">
                    <Input campo="Username" type="username" internal="div1" form={CreateRequest} add_function={add_function} />
                    <Input campo="Nome" type="Name" internal="div1" form={CreateRequest} add_function={add_function} />
                </div>
                <div className="two-inputs">
                    <Input campo="Sobrenome" type="surname" internal="div1" form={CreateRequest} add_function={add_function} />
                    <Input campo="CPF" type="CPF" internal="div1" form={CreateRequest} add_function={add_function} />
                </div>
                <div className="two-inputs">
                    <Input campo="Data_de_nascimento" type="Date" internal="div1" form={CreateRequest} add_function={add_function} />
                    <Input campo="Email" type="Email" internal="div1" form={CreateRequest} add_function={add_function} />
                </div>
                <div className="two-inputs">
                    <Input campo="Senha" type="Password" internal="div1" form={CreateRequest} add_function={add_function} />
                    <Input campo="Repetir_Senha" type="Password" internal="div1" form={CreateRequest} add_function={add_function} />
                </div>
                <div className="two-inputs">
                    <Input campo="Endereço" type="Address" internal="div1" form={CreateRequest} add_function={add_function} />
                    <Input campo="CEP" type="CEP" internal="div1" form={CreateRequest} add_function={add_function} />
                </div>
                <Button func={MakeRequest} text="signup" style={{ color: "black", fontSize: "30px" }} id="Cadastrar"/>
            </div>
        )
        return val
    }
}

export default SignUp