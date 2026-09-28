function berlinClock(time) {
    const [h, m, s] = time.split(':').map(Number);
  
    // Line 1: seconds — Y if even, O if odd
    const seconds = s % 2 === 0 ? 'Y' : 'O';
  
    // Line 2: four 5-hour lamps (red)
    const fiveHours = Array.from({ length: 4 }, (_, i) =>
      i < Math.floor(h / 5) ? 'R' : 'O'
    ).join('');
  
    // Line 3: four 1-hour lamps (red)
    const oneHours = Array.from({ length: 4 }, (_, i) =>
      i < h % 5 ? 'R' : 'O'
    ).join('');
  
    // Line 4: eleven 5-minute lamps (R every 3rd lit lamp, else Y)
    let fiveMinutes = '';
    const fiveMinCount = Math.floor(m / 5);
    for (let i = 0; i < 11; i++) {
      if (i < fiveMinCount) {
        fiveMinutes += (i + 1) % 3 === 0 ? 'R' : 'Y';
      } else {
        fiveMinutes += 'O';
      }
    }
  
    // Line 5: four 1-minute lamps (yellow)
    const oneMinutes = Array.from({ length: 4 }, (_, i) =>
      i < m % 5 ? 'Y' : 'O'
    ).join('');
  
    return [seconds, fiveHours, oneHours, fiveMinutes, oneMinutes].join('\n');
  }