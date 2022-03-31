function sumOfNonAbundantNumbers(n) {
  let abundantBelow = [];
  for (let i = 1; i <= n; i++) {
    if (isAbundant(i)) {
      abundantBelow.push(i);
    }
  }
  let abundantSums = [];
  for (let a of abundantBelow) {
    for (let b of abundantBelow) {
      let c = a + b;
      abundantSums.push(c);
    }
  }
  let uniqueSums = [...new Set(abundantSums)];
  let nonAbundantSums = [];
  for (let i = 1; i <= n; i++) {
    if (uniqueSums.indexOf(i) == -1) {
      nonAbundantSums.push(i);
    }
  }
  return nonAbundantSums.reduce((s, i) => s + i, 0);
}

function isAbundant(n) {
  return sumProperDivisors(n) > n;
}

function sumProperDivisors(n) {
  let result = 0;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i == 0) {
      if (i == n / i) {
        result += i;
      } else {
        result += i + n / i;
      }
    }
  }
  return result + 1;
}
console.time("p");
console.log(sumOfNonAbundantNumbers(28123));
console.timeEnd("p");
