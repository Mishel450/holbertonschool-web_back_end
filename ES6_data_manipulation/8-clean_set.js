export default function cleanSet(set, startString) {
  const { length } = startString;
  let stringToReturn = '';
  if (startString !== '') {
    for (const i of set) {
      const check = i.startsWith(startString);
      if (check === true) {
        stringToReturn += `${i.substring(length)}-`;
      }
    }
  }
  if (stringToReturn.endsWith('-')) {
    stringToReturn = stringToReturn.slice(0, -1);
  }
  return stringToReturn;
}
