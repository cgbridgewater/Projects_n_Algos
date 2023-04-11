

// Setting and Swapping
// Set myNumber to 42. Set myName to your name. Now swap myNumber into myName & vice versa.

    // var myNumber = 42;
    // var myName = "chris";``
    // var temp1 = myNumber;
    // var temp2 = myName;
    // myNumber = temp2;
    // myName = temp1;
    // console.log("name swapped " +myName);
    // console.log("number swapped " + myNumber);

// Print -52 to 1066
// Print integers from -52 to 1066 using a FOR loop.

//  for (i = -52; i <= 1066; i++) {
//     console.log(i);
//  }

// Don’t Worry, Be Happy
// Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.

// function beCheerful(num) { 
//  for (i = 0; i<= num; i++) {
//     console.log("good morning");
//  }
// }
// beCheerful(98);


// Multiples of Three – but Not All
// Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

// for (i = -300; i <= 0; i+=3){
//         if (i === -3|| i === -6 ){
//             console.log(" ");
//         }else
//         console.log(i);
// }


// Printing Integers with While
// Print integers from 2000 to 5280, using a WHILE.

// let i = 2000;
// while ( i <= 5280){
//     console.log(i);
//     i++
// }


// You Say It’s Your Birthday
// If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day...." 

//  for (i = 0; i <= 2000; i++){
//     if( i == 619 || i == 196 || i == 916 || i == 961 || i == 691 || i == 169){
//         console.log("how did you know " + i);
//     }
//     console.log("just another day");
//  }

// Leap Year
// Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.

// for (i = 0; i <= 2030; i++){
//     if((i % 4 == 0) && (i % 100 !=0) || (i % 400 ==0)){
//     console.log(i + " leap year");
//     } else {
//     console.log(i);
//     }
// }

// Print and Count
// Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.


// let count = 0
//  for (i = 512; i <= 4096; i++ ){
//     if (i % 5 == 0){
//         count ++ 
//     }
//  }
//  console.log(count);


// Multiples of Six
// Print multiples of 6 up to 60,000, using a WHILE.


// let i = 0
// while ( i <= 60000){
//     if (i %6 ==0){
//         console.log(i);
//         i++
//     } else {
//         i++
//     }
// }

// Counting, the Dojo Way
// Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

// for(i = 1; i <= 100; i++){
//     if(i % 10 == 0){
//         console.log('Coding Dojo')
//     } else if (i % 5 == 0){
//         console.log('Coding')
//     } else {
//         console.log(i)
//     }
// }

// What Do You Know?
// Your function will be given an input parameter incoming. Please console.log this value.

// function yourfunction(incoming){
//     console.log(incoming);
// }
// yourfunction('this value')

// Whoa, That Sucker’s Huge…
// Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?

//  var huge = 0

//  for( i= -300000; i<=300000; i++){
//     if( i % 2 !=0){
//         huge += 1
//     }
//  }
//  console.log(huge);

// var stillHuge = (Math.abs(-300000) + Math.abs(300000))/2
// console.log(stillHuge);


// Countdown by Fours
// Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.

 for( i = 2016; i > 0; i--){
    if(i % 4==0){
        console.log(i);
    }else {}
 }

// Flexible Countdown
// Based on earlier “Countdown by Fours”, given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).

 

// The Final Countdown
// This is based on “Flexible Countdown”. The parameter names are not as helpful, but the problem is essentially identical; don’t be thrown off! Given 4 parameters (param1,param2,param3,param4), print the multiples of param1, starting at param2 and extending to param3. One exception: if a multiple is equal to param4, then skip (don’t print) it. Do this using a WHILE. Given (3,5,17,9), print 6,12,15 (which are all of the multiples of 3 between 5 and 17, and excluding the value 9).

