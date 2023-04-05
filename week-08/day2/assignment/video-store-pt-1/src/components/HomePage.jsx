import InventoryItem from './InventoryItem';
import { useState} from 'react';
import DetailsPanel from './DetailsPanel';

export default function HomePage({ inventory }) {
    const [selectedTitle, setSelectedTitle] = useState(null);
    const selectedTitleByID = (id) => {
        if (id === null) {
            setSelectedTitle(null);
        }
        else {
            setSelectedTitle(inventory.find((item) => item.id === id));
        }
        }
    return (
        <>
            <h2>Inventory</h2>
            <div className="title_container">
                {
                    inventory.map(props => (<InventoryItem key={props.id} selectedTitleByID={selectedTitleByID}{...props} />))
                }
            </div>
           {selectedTitle && <DetailsPanel selected={selectedTitle}  /> }
        </>
    );
}