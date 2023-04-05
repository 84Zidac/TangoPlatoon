export default function DetailsPanel({selected}) {
    console.log(selected);
    const checkoutTitle = () => {
        selected.copiesAvailable.current-=1
        alert(`If you were to check out ${selected.title} there would now be ${selected.copiesAvailable.current - 1} copies available.`);
    };
    return(<div className="inventory_item">
                        <h3 className="item_title">{selected.title}</h3>
                        <img src={selected.imgUrl} height='250px' />
                        <div className="item_actions">
                        {selected.copiesAvailable.current} available
                            <button disabled={selected.copiesAvailable.current === 0}onClick={checkoutTitle}>{(selected.copiesAvailable.current === 0)? 'Unavaliable' : 'Checkout'}</button>
                        </div>
                        </div>)
}