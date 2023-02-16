import translate from "./pigLatin.js";

console.log("translates a word beginning with a vowel:");
console.log(translate("apple") === "appleay");

console.log("translates a word beginning with 'y':");
console.log(translate("your") === "ouryay");

console.log("translates a word beginning with a consonant:");
console.log(translate("banana") === "ananabay");

console.log("translates a word beginning with two consonants:");
console.log(translate("cherry") === "errychay");

console.log("translates two words:");
console.log(translate("eat pie") === "eatay iepay");

console.log("translates a word beginning with three consonants:");
console.log(translate("three") === "eethray");

console.log("counts 'sch' as a single phoneme:");
console.log(translate("school") === "oolschay");

console.log("counts 'qu' as a single phoneme:");
console.log(translate("quiet") === "ietquay");

console.log("counts 'qu' as a consonant even when it's preceded by a consonant:");
console.log(translate("square") === "aresquay");

console.log("translates many words:");
console.log(translate("the quick brown fox") === "ethay ickquay ownbray oxfay");

// write a test asserting that capitalized words are still capitalized
// (but with a different initial capital letter, of course) retain the
// punctuation from the original phrase
