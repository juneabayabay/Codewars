function toAcronym(inp) {
    return inp                    // "Code wars"
      .split(" ")                 // ["Code", "wars"]
      .map(word => word[0].toUpperCase()) // ["C", "W"]
      .join("");                  // "CW"
  }
  