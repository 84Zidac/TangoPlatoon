exports.factorial = function factoral(num) {
  if (num ===0 ){
    return 1
  }
  return num * factoral(num - 1)
  
};
