function binarySearch(num_to_find, array){
  // Code goes here!
  array.sort()
  let first = 0
  let middle = Math.floor(array.length/2)
  let last = array.length -1
    if (array[middle] === num_to_find){
      return middle
    }
    if (first === middle || last === middle){
      return -1
    }
    if (array[middle] > num_to_find){
      last = middle-1
      if (middle === Math.floor((last - first)/2))(
        middle--
      )
      else{
        middle = Math.floor((last - first)/2)
      }
    }
    if (array[middle] < num_to_find){
      first = middle
      if (middle === Math.floor((last + first)/2)){
        middle++
      }
      else{
        middle = Math.floor((last + first)/2)
      }
    }
  binarySearch(num_to_find, )

}

var smallArray = [1,2,3,4,5]
var largeArray = [1,5,7,2,3,8,4,9]

console.log(binarySearch(1, smallArray) === 0);
console.log(binarySearch(2, smallArray) === 1);
console.log(binarySearch(3, smallArray) === 2);
console.log(binarySearch(4, smallArray) === 3);
console.log(binarySearch(5, smallArray) === 4);
console.log(binarySearch(7, largeArray) === 5);
console.log(binarySearch(12, largeArray) === -1);
