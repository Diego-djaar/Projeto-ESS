import { ReactNode } from "react";
import { HomeProvider } from "./app/home/context/HomeContext";

const Provider = ({ children }: { children: ReactNode }) => {
  return <HomeProvider>{children}</HomeProvider>;
};

<<<<<<< Updated upstream
export default Provider;
=======
export default Provider;
>>>>>>> Stashed changes
