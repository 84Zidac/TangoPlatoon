async function pokemonGen() {
  let randomnum = parseInt(randnum(1008));
  let response = await axios.get(
    `https://pokeapi.co/api/v2/pokemon/${randomnum}`
  );
  let imageURL = response.data.sprites.front_default;
  addToHTML(imageURL, response.data.name);
  typeName = response.data.types[0].type.name;
  typeURL = response.data.types[0].type.url;
  let typeResponse = await axios.get(typeURL);
  let totalOfType = typeResponse.data.pokemon.length;
  console.log(typeResponse.data.pokemon);
  console.log(`master type: ${response.data.types[0].type.name}`);
  for (let i = 0; i < 5; i++) {
    let pokiNumToAdd = randnum(totalOfType);
    let addName = typeResponse.data.pokemon[pokiNumToAdd].pokemon.name;
    let newResponse = await axios.get(
      `https://pokeapi.co/api/v2/pokemon/${addName}`
    );
    let newImageURL = newResponse.data.sprites.front_default;
    console.log(
      `${newResponse.data.name} type: ${newResponse.data.types[0].type.name}`
    );
    addToHTML(newImageURL, newResponse.data.name);
  }
}
function randnum(num) {
  return Math.floor(Math.random() * num)+1;
}

function addToHTML(url, name) {
  let fig_cap = document.createElement('figure')  ;
  let image_element = document.createElement("img");
  let label_tag = document.createElement('figcaption');
  label_tag.innerText = name;
  image_element.src = url;
  image_element.id = name;
  image_element.alt = name;
  image_element.class = 'poki';
  fig_cap.id = 'fig'+name;
 
  document.getElementById('pokimons').appendChild(fig_cap);
  document.getElementById('fig'+name).appendChild(image_element);
  document.getElementById('fig'+name).appendChild(label_tag);
}
