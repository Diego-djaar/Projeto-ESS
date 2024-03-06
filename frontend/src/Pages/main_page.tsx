import { set_page } from "../Services/page_select"
import Button from "../Components/button";

export default function MainPage(props: {pageChanger: ()=> void}) {
    return (
        <div>
            <h1>
                placeholder text
            </h1>
            <Button func={() => { set_page("signup"); props.pageChanger(); }} text={"SignUp"} />
        </div>
    )
}