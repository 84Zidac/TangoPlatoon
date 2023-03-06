// let promise = fetch('https://pokeapi.co/api/v2/pokemon/') //Returns a promise
//     promise.then((response)=> response.json()) //transforms response to json
//     .then((data)=> console.log(data)) //
//     .catch(error=> console.log(error))

axios.get("https://pokeapi.co/api/v2/pokemon/12/") // returns a promise
  .then((response) => {
    let imageURL = response.data.sprites.front_default;
    console.log(imageURL);
    let image_element = document.createElement("img");
    image_element.src = imageURL;
    document.body.appendChild(image_element);
  });

async function callApi(){
    let response = await axios.get("https://pokeapi.co/api/v2/pokemon/12/")
    let imageURL = response.data.sprites.front_default
    let image_element = document.createElement('img')
    image_element.src = imageURL
    document.body.appendChild(image_element)
}