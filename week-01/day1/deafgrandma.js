function deafGrandma() {
  let goodbye = 0;
const prompt = require('prompt-sync')();
console.log('HEY KID!');
let kid = prompt();
while (goodbye < 1){
  if (kid === ""){
  console.log("WHAT?!");
  kid = prompt();
  }
  else if (kid == 'GOODBYE!' && goodbye < 1){
    console.log('LEAVING SO SOON?');
    goodbye += 1;
    kid = prompt();
  }
  else if (kid.toUpperCase() != kid){
    console.log('SPEAK UP, KID!');
    kid = prompt();
  }
  else if (kid.toUpperCase() == kid){
    console.log('NO, NOT SINCE 1946!');
    kid = prompt();
  }
}
return('LATER, SKATER!');
}

console.log(deafGrandma());