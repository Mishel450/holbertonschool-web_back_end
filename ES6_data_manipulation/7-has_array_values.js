export default function hasValuesFromArray(set, array) {
  for (const i of array) {
    const check = set.has(i);
    if (check === false) {
      return false;
    }
  }
  return true;
}
