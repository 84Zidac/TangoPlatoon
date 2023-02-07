function fib(num){
  let num1 = 0
  let num2 = 1
  let num3 = 1
  let count = 0
  while (num >= count){
    num3 = num2 + num1
    num2 = num1
    num1 = num3
    count ++
    console.log(num1)
    console.log(num2)
    console.log(num3)
  }
  return num2
}

console.log(fib(7))