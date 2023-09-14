export default function returnHowManyArguments(...arg) {
  let total = 0;
  for (let i = 0; i < arg.length; i) {
    total += 1;
  }
  return total;
}
