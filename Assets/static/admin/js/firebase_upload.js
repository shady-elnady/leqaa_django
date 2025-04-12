document.addEventListener("DOMContentLoaded", function () {
  // Handle image uploads
  const imageInputs = document.querySelectorAll(
    'input[type="file"][id^="id_firebase_image_url"]'
  );

  imageInputs.forEach((input) => {
    input.addEventListener("change", function (e) {
      const file = e.target.files[0];
      if (!file) return;

      // Show loading state
      const card = this.closest(".card");
      if (card) {
        card.innerHTML = `
                    <div class="text-center py-4">
                        <div class="spinner-border text-primary" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                        <p class="mt-2">Uploading image...</p>
                    </div>
                `;
      }

      // Here you would normally upload to Firebase
      // For this example, we'll simulate an upload
      setTimeout(() => {
        // This is where you would put your actual Firebase upload code
        // After upload, you would update the image URL
        const imageUrl = URL.createObjectURL(file);

        // Update the card with the new image
        if (card) {
          card.innerHTML = `
                        <img src="${imageUrl}" class="card-img-top" style="max-height: 200px; object-fit: contain;">
                        <div class="card-body">
                            <h5 class="card-title">New Image</h5>
                            <input type="file" name="${input.name}" class="form-control" id="${input.id}">
                        </div>
                    `;

          // Find the hidden input for the URL and update it
          const urlInput = document.querySelector(
            'input[name="firebase_image_url"]'
          );
          if (urlInput) {
            urlInput.value = imageUrl; // In real app, this would be the Firebase URL
          }
        }
      }, 1500);
    });
  });
});
