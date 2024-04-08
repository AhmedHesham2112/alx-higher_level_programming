#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined || isNaN(process.argv[3]) || process.argv[3] === undefined) {
  console.log(NaN);
} else {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
