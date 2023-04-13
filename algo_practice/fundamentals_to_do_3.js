// Biggie Size
// Given an array, write a function that changes all positive numbers in the array to “big”. Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,"big","big",-5].

// var arr = [-1,3,5,-5]
// var result = []
// function makeItBig(arr){
//     for(var i= 0; i< arr.length; i++){
//         if(arr[i] > 0){
//             arr[i] = "big";
//             result.push(arr[i]) 
//             continue
//         }
//         result.push(arr[i])
//     }
//     return result
// }

// makeItBig(arr)
// console.log(result);

// Print Low, Return High
// Create a function that takes an array of numbers. The function should print the lowest value in the array, and return the highest value in the array.

// var high = null
// var low = null
// function lowToHigh(arr){
//     for(var i= 0; i< arr.length; i++){

//         if( arr[i] < low ){
//             low = arr[i]
//         }
//         else if( arr[i] > high){
//             high = arr[i]
//         }
//     }
//     console.log(low);
//     return high
// }

// lowToHigh([8,6,7,5,3,0,9,-1])
// console.log("high number = "+ high);


// Print One, Return Another
// Build a function that takes an array of numbers. The function should print the second-to-last value in the array, and return first odd value in the array.

// var arr =[8,6,7,5,3,0,9,-1]
// function secondToLastOdd(arr){
//     console.log(arr[arr.length -2]);
//     for(var i = 0; i< arr.length; i++){
//         if( arr[i] % 2 != 0){
//             return arr[i]
//         }
//     }
// }
// var oddNum = secondToLastOdd(arr)
// console.log(oddNum);

// Double Vision
// Given an array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing original.


// newArr = []
// function doubleIt(arr){
//     for(var i= 0; i< arr.length; i++){
//         var temp = (arr[i] *2)
//         newArr.push(temp)
//     }
//     return newArr
// }
// console.log(result = doubleIt([1,2,3,4,5,6,7,8]));



// Count Positives
// Given an array of numbers, create a function to replace last value with the number of positive values. Example,  countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.
// var count = 0
// function posiCount(arr){
//     for(var i= 0; i< arr.length; i++){
//         if( arr[i] >0){
//             count ++
//         } 
//         arr[arr.length-1] = count
//     }
//     return arr
// }
// var result = posiCount([-1,1,1,1,-1,1,1,3])
// console.log(result);



// Evens and Odds
// Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"
// oddCount = 0
// evenCount = 0
// function thatsOdd(arr){
//     for(i = 0; i< arr.length; i++){
//         if (arr[i] %2 == 1 ){
//             evenCount =0
//             oddCount++
//             if(oddCount == 3){
//                 console.log("That's odd!");
//                 oddCount = 0
//             }
//         }
//         if (arr[i] % 2 ==0){
//             oddCount =0
//             evenCount++
//             if(evenCount == 3){
//                 console.log("Even more so!");
//                 evenCount = 0
//             }
//         }
//     }
// }
//     //    odd  //even//  //even//even//odd
// thatsOdd([1,3,5,6,4,2,1,3,4,4,6,6,4,4,4,3,3,3])


// Increment the Seconds
// Given arr, add 1 to odd elements ([1], [3], etc.), console.log all values and return arr.

// function addAnOdd(arr){
//     for( i= 0 ; i < arr.length ; i++){
//         if (i % 2 != 0){
//             arr[i] = (arr[i] + 1);
//             console.log(arr[i]);
//         }else
//         console.log(arr[i]);
//     }
//     return arr
// }

// var result = addAnOdd([9,6,4,2,1,3,4,4,7])
// console.log(result);

// Previous Lengths
// You are passed an array containing strings. Working within that same array, replace each string with a number – the length of the string at previous array index – and return the array.

// var temp = null;
// function previousLengths(arr){
//     for( i= 0 ; i < arr.length ; i++){
//         if( i == 0 ){
//             temp = arr[i]
//             arr[i] = arr[arr.length-1].length
//         }else {
//         temp1 = temp
//         temp = arr[i]
//         arr[i] = temp1.length
//     }
// }
// return arr
// }

// const result = previousLengths(['four', 'hit', 'ox', 'z','trees'])
// console.log(result);

// Add Seven to Most
// Build a function that accepts an array. Return a new array with all values except first, adding 7 to each. Do not alter the original array.

// newArr = []
// function plusSeven(arr){
//     for(var i= 0; i< arr.length; i++){
//         if( i == 0 ){
//         continue // move on to the next
//         }else
//         var temp = (arr[i] +7 )
//         newArr.push(temp)
//     }
//     return newArr
// }
// console.log(result = plusSeven([1,2,3,4,5,6,7,8]));

// Reverse Array
// Given array, write a function to reverse values, in-place. Example: reverse([3,1,6,4,2]) returns same array, containing [2,4,6,1,3].



// function flipFlop(arr){
//     for(var i=0; i<arr.length; i++){
//         if(i >= (arr.length/2)){
//             return arr
//         }
//         var temp1 = arr[i]
//         var temp2 = arr[arr.length-i-1]
//         arr[i] = temp2
//         arr[arr.length-i-1] = temp1
//     }
// }
// console.log(result = flipFlop([1,2,3,4,5,6,7,8,9,0]));


// Outlook: Negative
// Given an array, create and return a new one containing all the values of the provided array, made negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].

// function negativeOutlook(arr){
//     for(var i=0; i< arr.length; i++){
//         if (arr[i] <=0) continue
//         if (arr[i] > 0){
//             let temp = arr[i] *-1
//             arr[i] = temp
//         }
//     }
//     return arr
// }
// var result = negativeOutlook([1,-3,5])
// console.log(result);

// Always Hungry
// Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food". If no array elements are "food", then print "I'm hungry" once.

// var count = 0;
// function hangry(arr){
//     for(var i=0; i< arr.length; i++){
//         if( arr[i] == 'food'){
//             console.log("yummy!!");
//             count++
//         }
//     }
//     if (count == 0){
//         console.log("I'm getting Hangry!!");
//     }
// }
// // hangry(["table", "floor", "food", "chair", "food", "car", "schoolbus","food"])
// hangry(["table", "floor", "chair", "car", "schoolbus"])


// Swap Toward the Center
// Given array, swap first and last, third and third-tolast, etc. Input[true,42,"Ada",2,"pizza"] becomes ["pizza",42,"Ada",2,true].  Change [1,2,3,4,5,6] to [6,2,4,3,5,1].

// function swipSwap(arr){
//     for(var i=0; i<=arr.length; i++){
//         if(i >= (arr.length/2)){
//             return arr
//         }
//         if( i == 0){
//             var temp = arr[i]
//             arr[i] = arr[arr.length-i-1]
//             arr[arr.length-i-1] = temp
//         }
//         if( i == 2){
//             var temp = arr[i]
//             arr[i] = arr[arr.length-i-1]
//             arr[arr.length-i-1] = temp
//         }
//     }
// }
// console.log(result = swipSwap([1,2,3,4,5,6]));


// Scale the Array
// Given array arr and number num, multiply each arr value by num, and return the changed arr.

function upScale(arr, num){
    for(var i = 0; i<arr.length; i++){
        arr[i] = arr[i] * num
    }
    return arr
}
console.log(result = upScale([1,2,3,4,5,6], 3));