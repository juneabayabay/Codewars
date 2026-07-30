function trickyDoubles(num) {
    // Convert the number to a string
    const str = String(num);

    // If the number of digits is odd, it can't be a tricky double
    if (str.length % 2 !== 0) {
        return num * 2;
    }

    // Find the middle index
    const middle = str.length / 2;

    // Split the string into two halves
    const firstHalf = str.slice(0, middle);
    const secondHalf = str.slice(middle);

    // If both halves are identical, return the original number
    if (firstHalf === secondHalf) {
        return num;
    }

    // Otherwise, return double the number
    return num * 2;
}

// Test cases
console.log(trickyDoubles(15));      // 30
console.log(trickyDoubles(100));     // 200
console.log(trickyDoubles(4343));    // 4343
console.log(trickyDoubles(44));      // 44
console.log(trickyDoubles(7777));    // 7777
console.log(trickyDoubles(8787));    // 8787
console.log(trickyDoubles(100100));  // 100100
console.log(trickyDoubles(1212));    // 1212
console.log(trickyDoubles(1234));    // 2468