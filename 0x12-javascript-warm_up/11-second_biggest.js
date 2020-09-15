#!/usr/bin/node
// JS searches the second biggest

const args = process.argv.slice(2);
const argsInt = args.map(s => parseInt(s));
if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  console.log(argsInt.sort().reverse()[1]);
}
