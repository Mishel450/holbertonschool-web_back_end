export default function createInt8TypedArray(length, position, value) {
  const int8array = new Int8Array(length);
  if (position > length) {
    throw Error('Position outside range');
  }
  int8array[position] = value;
  const { buffer } = int8array;
  return new DataView(buffer, 0, length);
}
