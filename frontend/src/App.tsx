import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import PaymentConfig from "./app/home/pages/PaymentMethodsConfiguration";
import PaymentInserting from "./app/home/pages/PaymentInserting";

const router = createBrowserRouter([
  {
    path: "*",
    Component: CreateTest,
  },
  {
    path: "/create-test",
    Component: CreateTest,
  },
  {
    path: "/tests",
    Component: ListTests,
  },
  {
    path: "/paymentMethod", 
    Component: PaymentConfig,
  }, 
  {
    path: "/paymentMethod/inserting", 
    Component: PaymentInserting, 
  },
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
