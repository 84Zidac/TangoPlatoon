export default function InventoryItem({id, title, imgUrl, copiesAvailable, selectedTitleByID }) {
    

    return (
        <div className="inventory_item">
            <h3 className="item_title">{title}</h3>
            <img src={imgUrl} onClick={()=> selectedTitleByID(id)} />
            <div className="item_actions">
                {copiesAvailable.current} available

            </div>
        </div>
    );
}