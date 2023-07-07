// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!

function pushFront(arr,val){
    arr.push(val)
    for( var i= arr.length-1 ; i>0 ; i--)
        if( arr[i] == val){
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
        }
    return arr
}
console.log(result =  pushFront([6,7,5,3,0,9],8));
console.log(result =  pushFront([5,7,2,3],8));


function push(arr,val){
    for(let i = arr.length; i >= 0; i-- ){
        arr[i] = arr[i-1]
    }

    arr[0] = val

    return arr
}
console.log(push([5,7,2,3],8));

var arr = [1,2,3,4,5,6]
arr[6]= arr[5]
console.log(arr);


// Pop Front
// Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!


function popFront(arr){
    let temp = arr[0]
    for(var i = 0; i < arr.length-1; i++){
        arr[i] = arr[i+1] 
    }
    arr[arr.length-1] = temp
    arr.pop()
    console.log(arr);
    return temp
}

console.log(popFront([0,5,10,15]));
console.log(popFront([4,5,7,9]));

function popFront(arr){
    let temp = arr[0];
    for (var i =0; i < arr.length-1; i++){
        arr[i] = arr[i+1];
    }
    arr.length= arr.length-1;
    console.log(arr);
    return temp
}
console.log(popFront([0,5,10,15]));
console.log(popFront([4,5,7,9]));


// Insert At
// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!

Examples:

insertAt([100,200,5], 2, 311) //=> [100,200,311,5]
insertAt([9,33,7], 1, 42) //=> [9,42,33,7]


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


function insertedAt(arr,loc,val){
    for(let i = arr.length; i >= loc; i--){
        arr[i] = arr[i-1]
    }
    arr[loc] = val 
    return arr
}
console.log(insertedAt([100,200,5], 2, 311));
console.log(insertedAt([9,33,7], 1, 42));


// BONUS: Remove At
// Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it. Think of popFront(arr) as equivalent to removeAt(arr,0).

// Examples:

removeAt([1000,3,204,77], 1) //=> 3 returned, with [1000,204,77] printed in the function
removeAt([8,20,55,44,98], 3) //=> 44 returned, with [8,20,55,98] printed in the function


function removeAt(arr, idx){
    temp = arr[idx]
    for(let i = idx; i< arr.length; i++){
        arr[i] = arr[i+1]
    }
    arr.length--
    console.log(arr);
    return temp
}

console.log(removeAt([1000,3,204,77], 1));
console.log(removeAt([8,20,55,44,98], 3));



// BONUS: Swap Pairs
// Swap positions of successive pairs of values of given array. If length is odd, do not change the final element.

Examples:

insertAt([1,2,3,4]) //=> [2,1,4,3]
insertAt(["Brendan",true,42])//=> [true,"Brendan",42]

function insertAt(arr){
    for (let i = 0; i<arr.length-1; i++){
        if (i % 2 == 0){
            var temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
        }
    }
    return arr
}
console.log(insertAt([1,2,3,4]));
console.log(insertAt(["Brendan",true,42]));



// BONUS: Remove Duplicates
// Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. If you already made the Remove At function, you are welcome to use that! If you solved this using nested loops, for an extra challenge, try to do it without any nested loops!

// Examples:

removeDupes([-2,-2,3.14,5,5,10]) //=> [-2,3.14,5,10]
removeDupes([9,19,19,19,19,19,29])// => [9,19,29]



// NOT DONE

