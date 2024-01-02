// // Countdown
function countdown(num){
    result = [];
    for(var i = num; i >=0; i--){
        result.push(i);
    }
    return result;
}

console.log(countdown(5))

// // Print And Return
function print_and_return([num1,num2]){
    console.log("print ", num1);
    return "return " + num2;
}

console.log(print_and_return([1,2]))

// // First Plus Length
function first_plus_length(arr){
    return arr[0] + arr.length;
}

console.log(first_plus_length([1,2,3,4,5]))

// // This Length That Value
function length_and_value(num1,num2){
    newArr = [];
    for (let i = 0; i < num1; i++) {
        newArr.push(num2);
    }
    return newArr;
}

console.log(length_and_value(4,7));
console.log(length_and_value(6,2));

// // Values Greater Than Second
function values_greater_than_second(arr){
    newArr = [];
    length = arr.length;
    for(let i = 0; i< length; i++){
        if(length <2){
            return "False"
        }
        else {
            if(arr[i] > arr[1]){
                newArr.push(arr[i]);
            }
        }
    }
    return newArr;
} 

console.log(values_greater_than_second([5,2,3,2,1,4]));
console.log(values_greater_than_second([3]));