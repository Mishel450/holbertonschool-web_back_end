export default function getStudentsByLocation(arrstudents, city) {
  let arr = [];
  if (arrstudents instanceof Array) {
    arr = arrstudents.map((element) => {
      if (element.location === city) {
        return element;
      }

      return null;
    }).filter((result) => result !== null);
  }
  return arr;
}
