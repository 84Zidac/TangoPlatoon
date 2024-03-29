import axios from 'axios';
import { Link, useLoaderData } from 'react-router-dom';
import apiKey from '../data/apiKey.json';



export async function filmLoader({ params }) {
    const response = await axios.get(`https://www.omdbapi.com/?i=${params.filmId}&apikey=${apiKey}`);
    return response.data;
}

export default function DetailsPanel() {
    const filmData = useLoaderData();

    const { Title, Poster, Rated, Plot, Actors } = filmData;

    return (
        <div className="section_container">
            <Link to="/">Back to home page</Link>
            <h2>Details</h2>
            <div className="basic_container_column">
                <h3>{Title}</h3>
                <div className="basic_container_row align_center">
                    <img src={Poster} />
                    <p>{Plot}</p>
                    <div>{Actors}</div>
                    <pre style={{ fontSize: "40px" }}>{Rated}</pre>
                </div>
            </div>
        </div>
    );
}
