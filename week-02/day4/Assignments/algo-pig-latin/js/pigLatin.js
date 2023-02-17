/**
 * Translates a word, short phrase, or full sentence into pig latin.
 * @param {string} phrase - A single word, short phrase, or full sentence.
 * @returns {string} - The pig-latinified version of our phrase.
 */

const translate = function (phrase) {
  let vowels = ["a", "e", "i", "o", "u"];
  let str_return = "";
  let worker_str = "";
  for (let i = 0; i <= phrase.length; i++) {
    if (phrase[i] != " " && phrase[i] != undefined) {
      worker_str = worker_str + phrase[i];
    } else if (phrase[i] === " " || phrase[i] === undefined) {
      if (
        worker_str[0] + worker_str[1] === "qu" ||
        worker_str[1] + worker_str[2] === "qu"
      ) {
        let word_list1 = worker_str.split("");
        let ending = word_list1.splice(0, word_list1.indexOf("u") + 1);
        str_return = str_return + word_list1.join("") + ending.join("") + "ay ";
        worker_str = "";
      } else if (
        vowels.indexOf(worker_str[0]) == -1 &&
        vowels.indexOf(worker_str[1]) == -1 &&
        vowels.indexOf(worker_str[2]) == -1
      ) {
        let word_list = worker_str.split("");
        let first_letter = word_list.shift();
        let second_letter = word_list.shift();
        let third_letter = word_list.shift();
        let new_word =
          word_list.join("") +
          first_letter +
          second_letter +
          third_letter +
          "ay ";
        str_return = str_return + new_word;
        worker_str = "";
      } else if (vowels.indexOf(worker_str[0]) != -1) {
        str_return = str_return + worker_str + "ay ";
        worker_str = "";
      } else if (
        vowels.indexOf(worker_str[0]) == -1 &&
        vowels.indexOf(worker_str[1]) != -1
      ) {
        let word_list = worker_str.split("");
        let first_letter = word_list.shift();
        let new_word = word_list.join("") + first_letter + "ay ";
        str_return = str_return + new_word;
        worker_str = "";
      } else if (
        vowels.indexOf(worker_str[0]) == -1 &&
        vowels.indexOf(worker_str[1]) == -1
      ) {
        let word_list = worker_str.split("");
        let first_letter = word_list.shift();
        let second_letter = word_list.shift();
        let new_word =
          word_list.join("") + first_letter + second_letter + "ay ";
        str_return = str_return + new_word;
        worker_str = "";
      }
    }
  }
  let list_of_str = str_return.split("");
  list_of_str.pop();
  return list_of_str.join("");
};

// Export our function
export default translate;
