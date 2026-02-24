#!/usr/bin/node

const times = parseInt(process.argv[2]);

if (isNaN(times) || times < 1) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < times) {
    console.log('C is fun');
    i++;
  }
}
