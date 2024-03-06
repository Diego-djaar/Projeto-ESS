import App from "./app"
import ReactDOM from "react-dom/client"
import { page_atual } from "./Services/page_select"
import "./main.css"
const root = ReactDOM.createRoot(document.getElementById("root")!)
root.render(<App page_atual={page_atual!}/>)