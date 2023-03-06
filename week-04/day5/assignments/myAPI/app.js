let api_key = '&api_key=e50a92a8cb01d03b81d214b18d5b0dc15262d04f'
let api_secret = '&api_secret=5b47874454d9ec613a35365debbdd3dbb9d0fdbf'
let format = '&format=json'
async function iOtD(){
    let response = await axios.get(`http://astrobin.com/api/v1/imageoftheday/?limit=1${api_key}${api_secret}`);
    let returned = response.data
    print(returned)
}