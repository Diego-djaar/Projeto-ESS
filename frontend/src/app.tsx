import { createBrowserRouter, RouterProvider } from "react-router-dom";
import StoreSignUp from "/home/vitor/Documents/GitHub/Projeto-ESS/frontend/src/Pages/StoreSignUp";


const router = createBrowserRouter([
  {
    path: "/store/signup", 
    Component: StoreSignUp,
  }, 
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}