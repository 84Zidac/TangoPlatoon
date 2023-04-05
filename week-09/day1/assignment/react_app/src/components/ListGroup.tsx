// import { MouseEvent } from "react";

import { useState } from "react";

function ListGroup() {
  let items = [
    "New York",
    "San Francisco",
    "Detroit",
    "Pittsburgh",
    "Columbus",
  ];
  const [selectedIndex, setSelectedIndex] = useState(-1);

  return (
    <>
      <h1>List</h1>
      {items.length === 0 && <p>No item found</p>}
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            className={
              selectedIndex === index
                ? "list_group-item active"
                : "list_group-item"
            }
            key={item}
        //     onClick={() => {
        //       setSelectedIndex(index);
        //     }
        // }
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
