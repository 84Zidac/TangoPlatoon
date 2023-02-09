// function bottleSong(num){
//   bottles = num
//   while(bottles > 1){
//     console.log(`${bottles} bottles of beer on the wall, ${bottles} bottles of beer. Take one down and pass it around, ${bottles - 1} bottles of beer on the wall. `);
//     bottles-=1
//   }
//   if (bottles = 1){
//     console.log("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")
//   }

//   return("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

// }
// console.log(bottleSong(99))



function bottleSong(num){
  if (num === 0){
    console.log("No more bottles of beer on the wall, no more bottles of beer.");
  }
  else if (num === 1){
    console.log("1 bottle of beer on the wall, 1 bottle of beer.");
    console.log("Take one down and pass it around, no more bottles of beer on the wall.");
    bottleSong(num-1)
  }
  else{
    console.log(`${num} bottles of beer on the wall, ${num} bottles of beer.`) ;
    console.log(`Take one down and pass it around, ${num - 1} bottles of beer on the wall. `);;
    bottleSong(num-1)
  }
  return("Go to the store and buy some more, 99 bottles of beer on the wall.");
}
console.log(bottleSong(99))