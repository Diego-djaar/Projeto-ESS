import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import PaymentConfig from "./app/home/pages/PaymentMethodsConfiguration";
import PaymentInserting from "./app/home/pages/PaymentInserting";
import InsertingBoleto from "./app/home/pages/InsertingBoleto";
import InsertingPix from "./app/home/pages/InsertingPix";
import InsertingCard from "./app/home/pages/InsertingCard";

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
  {
    path: "/paymentMethod/inserting/boleto",
    Component: InsertingBoleto,
  },
  {
    path: "/paymentMethod/inserting/pix", 
    Component: InsertingPix
  }, 
  {
    path: "/paymentMethod/inserting/cartao", 
    Component: InsertingCard
  }
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
