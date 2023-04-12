// Countdown
// Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array?

// var number_array = []

// function countdown(zeroth){
//     for( i = zeroth; i >=0; i--){
//         number_array.push(i);
//     }
//     return number_array
// }

// countdown(10);
// console.log(number_array);
// console.log(number_array.length);


// Print and Return
// Your function will receive an array with two numbers. Print the first value, and return the second.

//  function twoNumbers(nums1,nums2){
//     console.log(nums1);
//     return nums2
//  }

//  twoNumbers(4,5);

// First Plus Length
// Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

// var sum

// function firstToLength(array){
//     sum = array[0] + array.length;
//     return sum
//  }

// firstToLength([8,6,7,5,3,0,9]);
// console.log(sum);


// Values Greater than Second
// For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.

// var arr = [1,3,5,7,9,13]
// var count = 0
// function checkValues(arr){
//     for(var i = 0; i < arr.length; i++){
//         if (arr[i] > arr[1]){
//             console.log("Value:" +arr[i]);
//             count ++
//         } else
//     }
//     return count;
// }
// checkValues(arr);
// console.log("Values greater than position 2: " +count);


// Values Greater than Second, Generalized
// Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?

// var arr = [1,3,5,7,9,13]
// var count = 0
// var result = []
// function checkValues(arr){
//     for(var i = 0; i < arr.length; i++){
//         if (arr[i] > arr[1]){
//             console.log("Value:" +arr[i]);
//             result.push(arr[i])
//             count ++
//         }
//     }
//     return count;
// }
// checkValues(arr);
// console.log("Values greater than position 2: " + count);
// console.log(result);

// This Length, That Value
// Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.



// Fit the First Value
// Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!"; if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".

// var arr = [7,6,7,5,3,0,9];
// function fittin(){
//     if(arr[0] > arr.length){
//         console.log("Too Big!");
//     } else if(arr[0] < arr.length){
//     console.log("Too Small!");
//     } 
//     console.log("Just Right!");
// }
// fittin(arr);



// Fahrenheit to Celsius
// Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit and returns the equivalent temperature as expressed in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.

// var fDegrees = 140;
// function convertToC(fDegrees){
//     var cDegrees = (fDegrees - 32)* 5/9
//     console.log(cDegrees);
// }
// convertToC(fDegrees)



// Celsius to Fahrenheit
// Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, and returns the equivalent temperature expressed in Fahrenheit degrees.


var cDegrees;
function convertToC(cDegrees){
    var fDegrees = (9/5 * cDegrees) + 32.
    console.log(fDegrees);
}
convertToC(40)


// (Optional): Do Fahrenheit and Celsius values equate at a certain number? The scientific calculation can be complex, so for this challenge just try a series of Celsius integer values starting at 200, going downward (descending), checking whether it is equal to the corresponding Fahrenheit value.
