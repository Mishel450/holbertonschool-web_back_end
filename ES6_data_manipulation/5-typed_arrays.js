export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const uint8array = new Uint8Array(buffer);
  if (position > length) {
    throw Error('Position outside range');
  }
  uint8array[position] = value;
  return buffer;
}
