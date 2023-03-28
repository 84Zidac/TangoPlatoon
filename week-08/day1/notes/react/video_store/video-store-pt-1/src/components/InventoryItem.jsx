export default function InventoryItem({ title, imgUrl, copiesAvailable }) {
    console.log(`from inventoryitem:Title:${title}, imgURL:${imgUrl}, Copies:${copiesAvailable}`)
    const checkoutTitle = () => {
        alert(`If you were to check out ${title} there would now be ${copiesAvailable - 1} copies available.`);
    };

    return (
            <div className="dropdown">
            <button className="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            {title}
            </button>
            <ul className="dropdown-menu">
                <li> <div className="inventory_item">
                        <h3 className="item_title">{title}</h3>
                        <img src={imgUrl} height='250px' />
                        <div className="item_actions">
                        {copiesAvailable} available
                            <button
                                disabled={copiesAvailable === 0}
                                onClick={checkoutTitle}
                            >{(copiesAvailable === 0)? 'Unavaliable' : 'Checkout'}</button>
                        </div>
                    </div></li>
            </ul>
            </div>

    );
}