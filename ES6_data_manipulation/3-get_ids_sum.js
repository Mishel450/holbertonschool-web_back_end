export default function getStudentIdsSum(students) {
  let arr = [];
  if (students instanceof Array) {
    arr = students.map((element) => element.id);
  }
  const sum = arr.reduce((acumulator, currentValue) => acumulator + currentValue, 0);
  return sum;
}
