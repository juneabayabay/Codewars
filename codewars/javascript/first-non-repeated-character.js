function firstNonRepeated(s) {
    // Check each character from left to right
    for (let char of s) {
        
        // If this character appears only once,
        // we found the first non-repeated character
        if (s.split(char).length - 1 === 1) {
            return char;
        }
    }

    // If every character is repeated, return null
    return null;
}
