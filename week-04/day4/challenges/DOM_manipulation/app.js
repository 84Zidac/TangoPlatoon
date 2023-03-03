function replaceImages() {
  console.log("yep it worked");
  const list_tags = document.body.getElementsByTagName("img");
  console.log(list_tags);
  for (let i = list_tags.length -1; i >= 0; i--) {
    let image = list_tags[i];
    if (image.alt) {
      let text = document.createTextNode(image.alt);
      image.parentNode.replaceChild(text, image);
    }
  }
}
