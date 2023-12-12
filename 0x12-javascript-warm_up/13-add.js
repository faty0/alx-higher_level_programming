#!/usr/bin/node

function add (a, b) {
  if (!isNaN(a)) {
    a = parseFloat(a);
  }
  if (!isNaN(b)) {
    b = parseFloat(b);
  }
  return (a + b);
}
module.exports = { add };
