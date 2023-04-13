// Fundamentals To Do 8


// Gaming Fun(damentals)
// It’s New Year’s Eve, so let’s play some dice games! It’ll be fun. What could go wrong?

// Create function rollOne() to return a randomly selected integer between 1 and 6 (inclusive).   
// Second, create a function playFives(num), which should call rollOne() multiple times –  ‘num' times, in fact, where 'num' is input parameter to playFives(num). Each time, it should print the value rollOne() returns, and if that return value is 5, also print “That’s good luck!”
// Third, create a new function named playStatistics(), which should call rollOne() eight times (but not print anything after each call). After the last of these eight calls, it should print out the lowest and highest values that it received from rollOne, among those eight calls.
// Fourth, make a copy of playStatistics and add code to make playStatistics2(), so that at the end (in addition to printing high/low rolls), it also prints the total sum of all eight rolls.
// Fifth, copy playStatistics2 and add code to it to make playStatistics3(num), so that it will roll as many times as you want, instead of always doing this eight times.
// Finally, make a copy of playStatistics3 and change it to create playStatistics4(num), so that at the end instead of the total sum, it prints the average roll.


// Statistics Until Doubles
// Here’s another game for our New Year’s Eve party. Implement a ’20-sided die’ that randomly returns integers between 1 and 20 inclusive. Roll these, tracking statistics until you get a value twice in a row. Display number of rolls, min, max, and average.




// Claire is Where?
// On New Year’s Eve, have fun but don’t forget your way home! For this challenge create four functions (reset, moveBy, xLocation and yLocation) to track the travels of Claire, a wanderer. Calling reset() moves Claire home to the origin (0,0). The moveBy(xOffset,yOffset) function moves her by those amounts, in those directions. Finally, xLocation() and yLocation()return how far Claire is from home, in X and Y directions respectively. After the calls of reset(), moveBy(1,-2), and moveBy(3,1), subsequently calling xLocation() and yLocation() should return 4 and -1.

// Second: create distFromHome(). Assuming she moves diagonally, return her distance from home.



// Date, on a Deserted Island
// After a particularly fabulous New Year’s Eve party to end 2016, Eduardo wakes to find himself stranded on a deserted island. He misses his home in Burbank, but at least now he can spend plenty of time outdoors – and you can’t beat the commute! To pass the time until he is rescued, he counts sunrises.

// Help Eduardo track what day of the week it is. Create a weekdayName(weekdayNum) function that, given a number between 1 and 7, will console.log a string containing the day of the week for that number (given 1, log "Sunday"). Use a SWITCH statement.
// Expand weekdayName() to create weekdayName2(dayNum) accepting numbers up to 365. Return weekday as before, given number of days total. "Sunday" still corresponds to 1.
// Create a new function someDays() that calls weekDayName2() seventeen times, with randomly generated integers as high as 365. Log each result string. If it is a weekday, add the phrase "Work hard!", and if it is a weekend day, add "Enjoy your day off!"
// Build function monthName(monthNum) that, given a number from 1 to 12, returns a string containing month for that number ("May" corresponds to 5). Use an array, without loops.
// Now expand monthName() to create monthToDays(monthNum), returning the number of days in that month, in the year 2017. Hint: use a SWITCH statement for the days in each month.
// Despite using his ember expertise to create a glowing SOS visible from space, the days go by and sadly Eduardo is still not rescued. Is it spring yet? It might as well be. Build on monthName() to create dayToMonth(dayNum). If given a day number since the year began, return the current month (assume it is not a Leap Year). Given 75, return "March".
// Eduardo builds a Dojo bootcamp on the island. Initially his students only find Ninja Gold in caves, but eventually, even his tree sloths can write code quickly! Dojo classes meet Monday thru Friday, so let’s reincorporate weekday to our calculations.  Construct fullDate(dayNum) to accept the number of days so far in 2017, and return a full date string. He hardly remembers that fateful New Year’s Eve party, but he knows it was a Saturday. Given 142, return "Monday, May 22, 2017".
// Times flies when you’re at a Dojo – months in fact. Build fullDate2(dayNum) that will be given a 4-digit integer: the days that have passed since December 31, 2016. This number can stretch into future years! You can assume that any year number divisible by four is a leap year and has a 29- day February. Given 8475, return "Thursday, March 15, 2040".
// Eduardo hacks the Google Maps API and adds this long-forgotten island back onto the map. Soon he is rescued! News of his Hemingway-like stoicism make him famous for centuries. Build fullDate3(dayNum) to handle days up to 140,000! Note: years 2100, 2200, and 2300 are not leap years (although 2400 is). Given 139947, return "Tuesday, February 29, 2400".
// Having completed this epic saga, you are ready for additional concepts and chapters! Journey safely….