import ClassRoom from './0-classroom';

function initializeRooms() {
  const clase1 = new ClassRoom(19);
  const clase2 = new ClassRoom(20);
  const clase3 = new ClassRoom(34);
  const arr = [clase1, clase2, clase3];
  console.log(arr);
}

initializeRooms();
