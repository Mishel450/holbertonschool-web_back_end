import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, filename) {
  return Promise.allSettled([uploadPhoto(filename), signUpUser(firstName, lastName)])
    .then((results) => {
      return results.map((result) => ({
        status: result.status,
        value: result.value
      }));
    });
}

export default handleProfileSignup;