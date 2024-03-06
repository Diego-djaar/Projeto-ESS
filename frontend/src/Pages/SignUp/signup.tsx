import Button from "../../Components/button"
import { set_page } from "../../Services/page_select"
import "./signup.css"
import Input from "../../Components/Input/inputs"

let SignUpForm = new Object()

function CreateRequest(entry: string, value: string) {
    console.log(entry, value)
}

export default function SignUp(props: {pageChanger: ()=> void}) {
    return (
    <div>
        <Button func={() => { set_page("main"); props.pageChanger(); }} text={"Back to main Page"}/>
            <h1 className="signup-text">Sign Up</h1>
            <div className="two-inputs">
                <Input campo="Username:" type="username" internal="div2" form={CreateRequest} />
                <Input campo="Nome:" type="Name" internal="div1"  form={CreateRequest} />
            </div>
            <div className="two-inputs">
                <Input campo="Sobrenome:" type="surname" internal="div2" form={CreateRequest} />
                <Input campo="CPF:" type="CPF" internal="div1" form={CreateRequest}  />
            </div>
            <div className="two-inputs">
                <Input campo="Data_de_nascimento:" type="Date" internal="div2" form={CreateRequest} />
                <Input campo="Email:" type="Email" internal="div1" form={CreateRequest} />
            </div>
            <div className="two-inputs">
                <Input campo="Senha:" type="Password" internal="div2" form={CreateRequest} />
                <Input campo="Repetir_Senha:" type="Password" internal="div1" form={CreateRequest} />
            </div>
            <div className="two-inputs">
                <Input campo="Endereço:" type="Address" internal="div2" form={CreateRequest} />
                <Input campo="CEP:" type="CEP" internal="div1" form={CreateRequest} />
            </div>
    </div>
    )
}