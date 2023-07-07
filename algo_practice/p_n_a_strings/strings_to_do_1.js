// Strings To Do 1
// Write functions using the JavaScript language for all challenges. Use only a single JavaScript file for this assignment. Do not use built-in methods (unless otherwise instructed). (.length is a property, and is allowed.)




// // // Remove Blanks
// Create a function that, given a string, returns all of that string’s contents, but without blanks. 


// // short cut!
function removeBlanks(string){
    var noblanks = string.split(" ")
    console.log(noblanks.join(""))
}


function removeBlanks(string){
    newString ='';
    for(let i =0; i< string.length; i++){
        if(string[i] !== ' '){
            newString += string[i]
        }
    }
console.log(newString);
}
// Examples:
removeBlanks(" Pl ayTha tF u nkyM usi c ")
removeBlanks("I can not BELIEVE it's not BUTTER")
//  => "PlayThatFunkyMusic"
//  => "IcannotBELIEVEit'snotBUTTER"




// // // Get Digits
// Create a JavaScript function that given a string, returns the integer made from the string’s digits. You are allowed to use isNaN() and Number().


function getDigits(string){
var digits = "";
    for(let i = 0; i < string.length; i++){
        if( isNaN(Number(string[i])) ){
        }else{
            digits +=string[i]
        }
    }
    console.log(digits);
}

// Examples:
getDigits("abc8c0d1ngd0j0!8")
getDigits("0s1a3y5w7h9a2t4?6!8?0")


// // // Acronyms
// Create a function that, given a string, returns the string’s acronym (first letter of the word capitalized). You are allowed to use .split() and .toUpperCase().


function acronym(string){
var acronym = ''
wordArray = string.split(" ")
// console.log(wordArray);
    for(let i = 0; i < wordArray.length; i++){
        if(wordArray[i][0] == undefined){
            
        }else
            acronym += wordArray[i][0].toUpperCase()
    }
    console.log(acronym);
}
acronym(" there's no free lunch - gotta pay yer way. ")
acronym("Live from New York, it's Saturday Night!")
//  => "TNFL-GPYW". 
//   => "LFNYISN".



// // // Count Non-Spaces
// Create a function that, given a string, returns the number of non-space characters found in the string. 

function countNonSpaces(string){
    count = 0;
    for(let i =0; i< string.length; i++){
        if(string[i] !== ' '){
            count++
        }
    }
console.log(count);
}
// Examples:
countNonSpaces("Honey pie, you are driving me crazy")
countNonSpaces("Hello world !")
//  => 29
//  => 11



Remove Shorter Strings
// Create a function that, given an array of strings and a numerical value, returns an array that only contains strings longer than or equal to the given value.


function removeShorterStrings(strings, val){
    const newArray = []
    for (let i = 0; i< strings.length; i++ ){
        if (strings[i].length >= val){ 
            newArray.push(strings[i])
        }
    }
return newArray
}

// Examples:
console.log( removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4) );
console.log( removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3) );
// => ['Good morning', 'sunshine', 'Earth', 'says', 'hello']
// => ['There', 'bug', 'the', 'system']