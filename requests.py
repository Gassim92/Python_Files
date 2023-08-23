import requests

url = "https://example.com/file_to_download.txt"
response = requests.get(url)

if response.status_code == 200:
    with open("downloaded_file.txt", "wb") as f:
        f.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download the file.")
