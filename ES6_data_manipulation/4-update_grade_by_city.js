export default function updateStudentGradeByCity(arrstudents, city, newGrades) {
  let arr = [];
  if (arrstudents instanceof Array) {
    arr = arrstudents.map((element) => {
      if (element.location === city) {
        let grades = 'N/A';
        newGrades.forEach((dict) => {
          if (element.id === dict.studentId) {
            grades = dict.grade;
          }
        });

        return { ...element, grades };
      }

      return null;
    }).filter((result) => result !== null);
  }
  return arr;
}
