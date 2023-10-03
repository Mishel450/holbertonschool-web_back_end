import { uploadPhoto } from "./utils";
import { createUser } from "./utils";

export default function handleProfileSignup() {
  const thephoto = uploadPhoto()
  const theuser = createUser()
  let photo_profile = ""
  let user_firstname = ""
  let user_lastname = ""
  let str = ""
  thephoto
    .then((photo) => {
      photo_profile = photo.body;
    });
  theuser
    .then((user) => {
      user_firstname = user.firstName;
      user_lastname = user.lastName;
      str = photo_profile + " "  + user_firstname + " " + user_lastname
      console.log(str)
    });
}