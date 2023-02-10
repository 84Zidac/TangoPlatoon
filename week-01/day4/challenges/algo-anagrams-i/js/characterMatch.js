exports.isCharacterMatch = function(string1, string2) {
 return string1.toLowerCase().replaceAll(' ', '').split('').sort().join('') === string2.toLowerCase().replaceAll(' ', '').split('').sort().join('')
};

exports.anagramsFor = function(word, listOfWords) {
  let answer = []
  for(let words of listOfWords){
    if (word.toLowerCase().replaceAll(' ', '').split('').sort().join('') === words.toLowerCase().replaceAll(' ', '').split('').sort().join('')){
      answer.push(words)
    }

  }
  return answer
};

