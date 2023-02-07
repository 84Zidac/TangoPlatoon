function TO_ROMAN(INPUT_NUMBER){
  let num = INPUT_NUMBER
  let output = ""
  const ROMAN_NUMERAL_TO_ARABIC_MAP = {M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1}
  let EVENLY_DIVISIBLE_TIMES = 0
  for(let key in ROMAN_NUMERAL_TO_ARABIC_MAP){
    console.log(num)
    console.log(key)
    console.log(ROMAN_NUMERAL_TO_ARABIC_MAP[key])
    EVENLY_DIVISIBLE_TIMES = num / ROMAN_NUMERAL_TO_ARABIC_MAP[key]
    console.log(EVENLY_DIVISIBLE_TIMES)
    while (EVENLY_DIVISIBLE_TIMES >= 1){
      output = output + key
      num = num - ROMAN_NUMERAL_TO_ARABIC_MAP[key]
      EVENLY_DIVISIBLE_TIMES-=1
    }
  }






  return(output) 
}




console.log(TO_ROMAN(4))