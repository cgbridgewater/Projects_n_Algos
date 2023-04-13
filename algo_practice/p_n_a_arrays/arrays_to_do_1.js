


// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!

// function pushFront(arr){
//     arr.push(1)
//     for( var i= arr.length-1 ; i>0 ; i--)
//         if( arr[i] == 1){
//             temp = arr[i]
//             arr[i] = arr[i-1]
//             arr[i-1] = temp
//         }
//     return arr
// }
// // var result =  pushFront([5,7,2,3])
// var result =  pushFront([2,3,4,5,6,7])
// console.log(result);



// Pop Front
// Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!


// function popFront(arr){
//     var temp
//     for(var i = 0; i < arr.length-1; i++){
//         if( i == 0){
//             temp = arr[0]
//         }
//         arr[i] = arr[i+1] 
//     }
//     arr[arr.length-1] = temp
//     arr.pop()
//     console.log(arr);
//     return temp
// }

// console.log(result = popFront([0,5,10,15]));
// console.log(result = popFront([4,5,7,9]));




// Insert At
// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!

// Examples:

// insertAt([100,200,5], 2, 311) => [100,200,311,5]
// insertAt([9,33,7], 1, 42) => [9,42,33,7]


function insertAt(arr, loc, val){
    arr.push(val)
    for(var i = arr.length-1; i > loc; i-- )
        if(i != loc){
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = temp
        }
        return arr
}

console.log(result= insertAt([100,200,5], 2, 311));
console.log(result= insertAt([9,33,7], 1, 42));



// BONUS: Remove At
// Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it. Think of popFront(arr) as equivalent to removeAt(arr,0).

// Examples:

// removeAt([1000,3,204,77], 1) => 3 returned, with [1000,204,77] printed in the function
// removeAt([8,20,55,44,98], 3) => 44 returned, with [8,20,55,98] printed in the function
// 






// BONUS: Swap Pairs
// Swap positions of successive pairs of values of given array. If length is odd, do not change the final element.

// Examples:

// insertAt([1,2,3,4]) => [2,1,4,3]
// insertAt(["Brendan",true,42]) => [true,"Brendan",42]








// BONUS: Remove Duplicates
// Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. If you already made the Remove At function, you are welcome to use that! If you solved this using nested loops, for an extra challenge, try to do it without any nested loops!

// Examples:

// removeDupes([-2,-2,3.14,5,5,10]) => [-2,3.14,5,10]
// removeDupes([9,19,19,19,19,19,29]) => [9,19,29]