import App from "./App"
import ReactDOM from "react-dom/client"
import { page_atual } from "./Services/page_select"
import "./main.css"
import { CpfProvider } from "./Context/CpfContext"
const root = ReactDOM.createRoot(document.getElementById("root")!)
root.render(
    <CpfProvider>
        <App page_atual={page_atual!} />
    </CpfProvider>
)