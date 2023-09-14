export default function returnHowManyArguments() {
  let total = 0;
  for (let i = 0; i < arguments.length; i) {
    total += 1;
  }
  return total;
}
