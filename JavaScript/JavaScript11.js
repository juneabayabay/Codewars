function lettersToNumbers(s) {
    let total = 0;
  
    for (let char of s) {
      let code = char.charCodeAt(0);
  
      // Lowercase a-z
      if (code >= 97 && code <= 122) {
        total += code - 96;
      }
      // Uppercase A-Z
      else if (code >= 65 && code <= 90) {
        total += (code - 64) * 2;
      }
      // Digits 0-9
      else if (code >= 48 && code <= 57) {
        total += code - 48;
      }
      // Other characters add 0 (do nothing)
    }
  
    return total;
  }