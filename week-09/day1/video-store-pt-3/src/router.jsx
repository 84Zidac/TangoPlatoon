import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./components/HomePage";
import DetailsPanel from "./components/DetailsPanel";
import InventoryItem from "./components/InventoryItem";
// import PokeViewer, { pokeLoader } from "./components/PokeViewer";

const router = createBrowserRouter([
    {
        path: "/",
        element: < App />,
        errorElement: <ErrorPage />,
        children: [
            {
                index: true,
                element: <HomePage />
            },
            {
                path: "details/:id",
                element: <AboutPage />
            }
            // {
            //     path: "pokemon/:pokeId",
            //     element: <PokeViewer />,
            //     loader: pokeLoader
            // }
        ]
    }
]);

export default router;