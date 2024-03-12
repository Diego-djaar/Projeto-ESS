import { set_page } from "../../Services/page_select"
import Button from "../../Components/Button/button";

export default function MainPage() {
    return (
        <div>
            <h1>
                placeholder text
            </h1>
            <Button func={() => set_page("signup")} text={"SignUp"} style={{}} id={""} />
            <Button func={() => set_page("carrinho")} text={"Carrinho"} style={{}} id={""} />
        </div>
    )
}