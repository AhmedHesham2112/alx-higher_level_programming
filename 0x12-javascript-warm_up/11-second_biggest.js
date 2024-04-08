#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined || isNaN(process.argv[3]) || process.argv[3] === undefined) {
  console.log(0);
} else {
  let big = parseInt(process.argv[2]);
  let small = parseInt(process.argv[3]);
  if (parseInt(process.argv[2]) > parseInt(process.argv[3])) {
    big = parseInt(process.argv[2]);
    small = parseInt(process.argv[3]);
  } else {
    big = parseInt(process.argv[3]);
    small = parseInt(process.argv[2]);
  }
  for (let i = 4; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > big) {
      small = big;
      big = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) < big && parseInt(process.argv[i]) > small) {
      small = parseInt(process.argv[i]);
    }
  }
  console.log(small);
}
