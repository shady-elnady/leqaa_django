import requests

# Assuming you have your API endpoint URL
api_url = "http://your-domain.com/api/categories/"
token = "YOUR_AUTH_TOKEN"  # Your authentication token

with open("path/to/your/image.jpg", "rb") as image_file:
    files = {"image": image_file}
    data = {
        "name": "New Category Name",
        "translations": {
            "en": "New Category Name in English",
            "fr": "Nouveau Nom de Catégorie",
        },
    }
    headers = {"Authorization": f"Token {token}"}
    response = requests.post(api_url, files=files, data=data, headers=headers)

    if response.status_code == 201:
        print("Category created successfully!")
        print(response.json())
    else:
        print(f"Error creating category: {response.status_code}")
        print(response.text)
