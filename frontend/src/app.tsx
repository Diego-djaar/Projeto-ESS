import { Component } from "react";
import MainPage from "./Pages/main_page"
import SignUp from "./Pages/SignUp/signup"
import { page_atual } from "./Services/page_select";

class App extends Component {
    props: {page_atual: string}
    constructor(props: {page_atual: string}) {
        super(props);
        this.props = props;
        this.state = { page_atual: page_atual }
        this.reload = this.reload.bind(this)
    }

    reload() {
        this.setState({
            page_atual: page_atual
        })
    }

    render() {
        return (
            <div>
                {page_atual === "main" && <MainPage pageChanger={this.reload} />}
                {page_atual === "signup" && <SignUp pageChanger={this.reload} />}
            </div>
        );
    }
}
export default App;