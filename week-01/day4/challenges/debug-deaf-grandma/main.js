let stillTalking = true
let goodbyes = 0
while ( stillTalking ) {

    let userInput = prompt()
    
    if ( userInput == "" ) {
        alert("WHAT!?")
    }
    else if ( userInput.toUpperCase() != userInput ) {
        alert('SPEAK UP, KID!')
    }
    else if ( userInput.toUpperCase() == userInput && userInput !=  "GOODBYE!") {
        alert('NO, NOT SINCE 1946!')
    }
    else if ( userInput == "GOODBYE!" ) {
        goodbyes += 1

        if ( goodbyes == 1 ) {
            alert('LEAVING SO SOON?')
        }
        else if ( goodbyes == 2 ) {
            alert("LATER, SKATER!")
            stillTalking = false
        }
    }
    
}