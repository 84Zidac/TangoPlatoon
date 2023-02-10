// exports.
sum_pairs = function(arr, num) {
let ansArr = []
for (let i = 0; i < arr.length; i++){
  for (let j = 1; j < arr.length; j++){
    if (arr[i] + arr[j] === num){
      ansArr.push([arr[i], arr[j]])
    }
  }
}
return ansArr
};
console.log(sum_pairs([1,2,3,4,5], 9)) 
console.log(sum_pairs([1,2,3,4,5], 7)) 