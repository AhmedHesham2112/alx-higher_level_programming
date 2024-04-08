#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log(1);
} else {
  let n = 1;
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
  n = n * i;
  }
  console.log(n);
}
