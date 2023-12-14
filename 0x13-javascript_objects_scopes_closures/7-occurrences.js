#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let oc = 0;
  list.forEach(element => {
    if (element === searchElement) {
      oc++;
    }
  });
  return oc;
};
