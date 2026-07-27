function toNato(words) {
    let result = [];
  
    for (let ch of words) {
      if (ch === " ") {
        continue;
      } else if (/[A-Za-z]/.test(ch)) {
        result.push(NATO[ch.toUpperCase()]);
      } else {
        result.push(ch);
      }
    }
  
    return result.join(" ");
  }