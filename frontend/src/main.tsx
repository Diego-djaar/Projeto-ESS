import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./global.css";
import Provider from "./Provider";
import { CpfProvider } from "./app/home/context/HomeContext/CpfContext";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <Provider>
      <CpfProvider>
        <App />
      </CpfProvider>
    </Provider>
  </React.StrictMode>
);
