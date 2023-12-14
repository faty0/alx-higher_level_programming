#!/usr/bin/node
exports.esrever = function (list) {
  const l = list.length - 1;
  let j = 0;
  const list2 = [];
  if (l > 0) {
    for (let i = l; i >= 0; i--) {
      list2[j] = list[i];
      j++;
    }
  }
  return list2;
};
