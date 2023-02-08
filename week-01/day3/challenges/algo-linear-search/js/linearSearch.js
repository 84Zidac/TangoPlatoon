const arrayToSearchThrough = [];
for (let i = 1; i <= 1000; i++) {
    arrayToSearchThrough.push(i);
}

exports.linearSearch = function(valueToFind, arrayToSearchThrough) {
    for (let i = 0; i < arrayToSearchThrough.length; i++){
        if (arrayToSearchThrough[i] === valueToFind){
            return i
        }
    }
    return undefined
};

exports.linearSearchGlobal = function(valueToFind, arrayToSearchThrough) {
    let answer = []
    for (let i = 0; i < arrayToSearchThrough.length; i++){
        if (arrayToSearchThrough[i] === valueToFind){
            answer.push(i)
        }
    }
    return answer
};