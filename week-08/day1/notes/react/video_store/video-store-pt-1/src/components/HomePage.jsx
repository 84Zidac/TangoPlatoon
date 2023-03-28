import InventoryItem from './InventoryItem';

export default function HomePage({ inventory }) {
    console.log(inventory);
    return (
        <>
            <marquee scrollamount="1" behavior="alternate">Inventory<div class="spinner-border text-warning" role="status">
  <span class="visually-hidden">Loading...</span>
</div></marquee>

            <div className="title_container">
                {
                    inventory.map(props => <InventoryItem {...props} />)
                }
            </div>
        </>
    );
}

