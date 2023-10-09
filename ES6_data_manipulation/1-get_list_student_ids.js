export default function getListStudentsIds(getListStudents) {
  let arr = [];
  if (getListStudents instanceof Array) {
    arr = getListStudents.map((element) => element.id);
  }
  return arr;
}
