export default function updateStudentGradeByCity(arrstudents, city, newGrades) {
  let arr = [];
  if (arrstudents instanceof Array) {
    arr = arrstudents.map((element) => {
      if (element.location === city) {
        let grade = 'N/A';
        newGrades.forEach((dict) => {
          if (element.id === dict.studentId) {
            grade = dict.grade;
          }
        });

        return { ...element, grade };
      }

      return null;
    }).filter((result) => result !== null);
  }
  return arr;
}
