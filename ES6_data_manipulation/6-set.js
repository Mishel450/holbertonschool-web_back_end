export default function setFromArray(values) {
  const theset = new Set();
  for (let i of values) {
    theset.add(i)
  }
  return theset
}