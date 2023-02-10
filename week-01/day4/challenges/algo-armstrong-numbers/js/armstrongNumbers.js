// How can you make this more scalable and reusable later?

//exports.
findArmstrongNumbers = function(numlist) {
let answer = []
for (let i = 0; i < numlist.length; i++){
  let len = numlist[i].toString().length
  let count = len-1
  let sum = 0
  while(count >= 0){
   sum += Number(numlist[i].toString()[count]) ** len
   count--
  }
  if (numlist[i] === sum){
    answer.push(sum)
  }
}
return answer
};






function createArrayOfNum(maxValue) {
  return Array.apply(null, {length: maxValue}).map(Number.call, Number)
}

 console.log(findArmstrongNumbers([0]));
console.log(findArmstrongNumbers(createArrayOfNum(99)))//, [0, 1, 2, 3, 4, 5, 6, 7]));
console.log(findArmstrongNumbers(createArrayOfNum(9999)))//, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
// console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(999)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]));




