function factoral(num){
  let newnum = num
  let answer = 1
  while (newnum > 1){
    answer = answer * newnum
    newnum -=1
  }
  return answer
}


console.log(factoral(4))