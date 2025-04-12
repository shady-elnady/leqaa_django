import { getStorage, ref, uploadBytes, getDownloadURL } from "firebase/storage";
import { getAuth } from "firebase/auth";
import { app } from "./firebaseConfig"; // Assuming you have initialized Firebase in firebaseConfig.js

async function uploadImageToFirebaseStorage(file) {
  const auth = getAuth(app);
  const storage = getStorage(app);
  const user = auth.currentUser;

  if (!user) {
    console.error("User is not authenticated.");
    return null; // Or throw an error, depending on your error handling strategy
  }

  const userId = user.uid;
  const imageName = `${Date.now()}_${file.name}`; // Use a unique name
  const storageRef = ref(storage, `my_images/${userId}/${imageName}`); // Path in Storage

  try {
    const snapshot = await uploadBytes(storageRef, file);
    console.log("Uploaded a blob or file!");

    // Get the download URL
    const downloadURL = await getDownloadURL(snapshot.ref);
    console.log("Download URL:", downloadURL);
    return downloadURL;
  } catch (error) {
    console.error("Error uploading image:", error);
    return null; // Or throw the error
  }
}

// Example usage:
async function handleImageUpload(event) {
  const file = event.target.files[0]; // Assuming you have an input element for file selection
  if (file) {
    const downloadUrl = await uploadImageToFirebaseStorage(file);
    if (downloadUrl) {
      console.log("Image uploaded successfully. Download URL:", downloadUrl);
      // You can now save this downloadURL to your database
    } else {
      console.log("Failed to upload image.");
    }
  }
}

// --- HTML for file input (example) ---
/*
<input type="file" id="imageUpload" accept="image/*">
<button onclick="document.getElementById('imageUpload').click()">Upload Image</button>

<script>
  document.getElementById('imageUpload').addEventListener('change', handleImageUpload);
</script>
*/

// --- firebaseConfig.js (example - make sure to replace with your actual config) ---
/*
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

const app = initializeApp(firebaseConfig);

export { app };
*/
