function add(arr) {
    let result = [];
    let sum = 0;
  
    for (let num of arr) {
      sum += num;
      result.push(sum);
    }
  
    return result;
  }