function rotations(dieArray) {
    const opposite = {
      1: 6,
      2: 5,
      3: 4,
      4: 3,
      5: 2,
      6: 1
    };
  
    let minRotations = Infinity;
  
    for (let target = 1; target <= 6; target++) {
      let rotationsNeeded = 0;
  
      for (const die of dieArray) {
        if (die === target) {
          // Already showing the target
          continue;
        }
  
        if (opposite[die] === target) {
          // Opposite face requires 2 rotations
          rotationsNeeded += 2;
        } else {
          // Adjacent face requires 1 rotation
          rotationsNeeded += 1;
        }
      }
  
      minRotations = Math.min(minRotations, rotationsNeeded);
    }
  
    return minRotations;
  }
  