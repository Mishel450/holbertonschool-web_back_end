import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const thephoto = uploadPhoto();
  const theuser = createUser();
  let photoprofile = '';
  let userfirstname = '';
  let userlastname = '';
  let str = '';
  thephoto
    .then((photo) => {
      photoprofile = photo.body;
    })
    .catch(() => Error('Signup system offline'));
  theuser
    .then((user) => {
      userfirstname = user.firstName;
      userlastname = user.lastName;
      str = `${photoprofile} ${userfirstname} ${userlastname}`;
      console.log(str);
    })
    .catch(() => Error('Signup system offline'));
}
