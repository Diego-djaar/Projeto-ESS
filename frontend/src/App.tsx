import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import StoreSignUp from "./Pages/StoreSignUp";
import StoreLogin from "./Pages/StoreLogin";
import StoreRetrieve from "./Pages/StorePassRetrieve";
import StoreUpdate from "./Pages/StoreUpdate";

const router = createBrowserRouter([
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
  },
  {
    path: "/stores/update_store",
    Component: StoreUpdate,
  },
  // {
  //   path: "*",
  //   Component: CreateTest,
  // },
  // {
  //   path: "/create-test",
  //   Component: CreateTest,
  // },
  // {
  //   path: "/tests",
  //   Component: ListTests,
  // },
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
