import Button from "../../Components/Button/button"
import { set_page } from "../../Services/page_select"
import "./login.css"
import Input from "../../Components/Input/inputs"
import { CreateLoginRequest, MakeLoginRequest, add_function, Init } from "../../Services/login"
import { Component } from "react"

export default class Login extends Component{

    componentDidMount() {
        Init();
    }

    render() {
        const val = (
            <div>
                <Button func={() => set_page("main")} text={"Back to main Page"} style={{}} id="Main" />
                <Button func={() => set_page("signup")} text={"SignUp"} style={{}} id={""} />
                <h1 className="login-text">Login</h1>
                <div className="two-inputs">
                    <Input campo="CPF_ou_User_ou_Email" type="username" internal="div1" form={CreateLoginRequest} add_function={add_function} />
                    <Input campo="Senha" type="Password" internal="div1" form={CreateLoginRequest} add_function={add_function} />
                </div>
                
                <Button func={MakeLoginRequest} text="login" style={{ color: "black", fontSize: "30px" }} id="Login"/>      
            </div>
        )
        return val
    }
}