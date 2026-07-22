function filter_list(l) {               // Create a function that takes an array called l.

    let result = [];                    // Create an empty array to store only the numbers.

    for (let i = 0; i < l.length; i++) { // Loop through every item in the array.

        if (typeof l[i] === "number") { // Check if the current item is a number.

            result.push(l[i]);          // If it is a number, add it to the result array.

        }

    }

    return result;                      // Return the new array containing only numbers.

}