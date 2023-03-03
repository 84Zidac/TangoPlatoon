function num_gen() {
    let rannum = Math.floor(Math.random()*100);
    return rannum
}

// const randomnum = gen_num()
function guessChecker() {

    let userReply = document.getElementById("reply");
    let guess = parseInt(document.getElementById('input').value)
    let winner = document.getElementById('carlton')

    if (!Number.isInteger(guess)){
        userReply.removeAttribute("hidden")
        userReply.innerHTML = `Guess needs to be between 0 and 100`

        return
    }

    console.log(guess);
    console.log(rannum);
    if (guess > rannum) {
        userReply.removeAttribute("hidden")
        userReply.innerHTML = `<b>${guess} is too high</b>`
    } else if (guess < rannum) {
        userReply.removeAttribute("hidden")
        userReply.innerHTML = `<b>${guess} is too low</b>`
    } else {
        userReply.removeAttribute("hidden")
        userReply.style.background = 'green'
        winner.removeAttribute('hidden')
        userReply.innerHTML = "<b>You guessed it!</b>"
    }
 
}


const rannum = num_gen()
// Your function(s) should go here that will interact with the webpage or DOM
/* <body>
<!-- your HTML should go here -->
<nav>
  <h1>Let's Play the Guessing Number Game!</h1>
</nav>
<input id="input" type="text">
<button type="button" onclick="guesChecker()">Submit Guess</button>
<div id="reply"></div>

</body> */

