import { useLoaderData } from 'react-router-dom';
import axios from 'axios';
import InventoryItem from './InventoryItem';
import inventory from '../data/inventory.json';
import apiKey from '../data/apiKey.json';
import Cards from './Cards'

export async function allFilmsLoader() {
    const promises = inventory.map(imdbId => axios.get(`https://www.omdbapi.com/?i=${imdbId}&apikey=${apiKey}`));
    const responses = await Promise.all(promises);
    const allFilmData = responses.map(response => response.data);
    return allFilmData;
}

export default function HomePage() {

    const allFilmData = useLoaderData();
    console.log(allFilmData);

    return (
        <div className="page_container">
            <h2>Inventory</h2>
            <div className="section_container">
                {
                    
                        <Cards
                            filmData={allFilmData}
                        />
                   
                }
            </div>
        </div>
    );
}


