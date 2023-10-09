export default function setFromArray(values) {
  const theset = new Set();
  for (const i of values) {
    theset.add(i);
  }
  return theset;
}
