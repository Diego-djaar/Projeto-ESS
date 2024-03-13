import { createBrowserRouter, RouterProvider } from "react-router-dom";
import ViewCart from "./Pages/Carrinho";
import ItemPage from "./Pages/ItemPage";
import MainPage from "./Pages/MainPage/main_page"
import SignUp from "./Pages/SignUp/signup"
import { Component } from "react";
import { page_atual, refresh_window_assign } from "./Services/page_select";
import Login from "./Pages/Login/login"
import User from "./Pages/User/user";
import UpdateUser from "./Pages/UpdateUser/update";
import Inventory from "./inventory";
import AddItem from "./add_item";
import StoreSignUp from "./Pages/StoreSignUp";
import StoreLogin from "./Pages/StoreLogin";
import StoreRetrieve from "./Pages/StorePassRetrieve";
import StoreUpdate from "./Pages/StoreUpdate";

const router = createBrowserRouter([
  {
    path: "/",
    Component: MainPage
  },
  {
    path: "/main",
    Component: MainPage
  },
  {
    path: "/signup",
    Component: SignUp
  },
  {
    path: "/login",
    Component: Login
  },
  {
    path: "/inventory",
    Component: Inventory,
  },
  {
    path: "/inventory/add_item/:CNPJ",
    Component: AddItem,
  },
  {
    path: "/user",
    Component: User
  },
  {
    path: "/update_user",
    Component: UpdateUser
  },
  {
    path: "/carrinho",
    Component: ViewCart,
  },
  {
    path: "/itempage",
    Component: ItemPage,
  }
  {
    path: "/stores/signup",
    Component: StoreSignUp,
  },
  {
    path: "/stores/login",
    Component: StoreLogin,
  },
  {
    path: "/stores/retrieve_password",
    Component: StoreRetrieve,
    
>>>>>>> development
  },
  {
    path: "/stores/update_store",
    Component: StoreUpdate,
  },
]);

class App extends Component {
    props: {page_atual: string}
    constructor(props: {page_atual: string}) {
        super(props);
        this.props = props;
        this.state = { page_atual: page_atual }
        this.reload = this.reload.bind(this)
        refresh_window_assign(this.reload)
    }

    reload() {
      window.location.href = '/' + page_atual;
      this.setState({
          page_atual: page_atual
      })
    }

    render() {
        return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
    }
}
export default App;


class App extends Component {
    props: {page_atual: string}
    constructor(props: {page_atual: string}) {
        super(props);
        this.props = props;
        this.state = { page_atual: page_atual }
        this.reload = this.reload.bind(this)
        refresh_window_assign(this.reload)
    }

    reload() {
      window.location.href = '/' + page_atual;
      this.setState({
          page_atual: page_atual
      })
    }

    render() {
        return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
    }
}
export default App;


