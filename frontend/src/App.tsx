import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import Inventory from "./inventory";
import AddItem from "./add_item";

const router = createBrowserRouter([
  {
    path: "/inventory",
    Component: Inventory,
  },
  {
    path: "/inventory/add_item/:CNPJ",
    Component: AddItem,
  },
  {
    path: "/create-test",
    Component: CreateTest,
  },
  {
    path: "/tests",
    Component: ListTests,
  },
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
