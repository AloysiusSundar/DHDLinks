import os
import requests
import urllib.parse

def create_filename(url):
    # Parse the URL
    parsed_url = urllib.parse.urlparse(url)
    
    # Extract the path and query
    path = parsed_url.path
    query = parsed_url.query
    
    # Create a valid filename from the path and query
    base_filename = os.path.basename(path)  # Get the last part of the path
    if query:  # Append query parameters if they exist
        query_encoded = urllib.parse.quote(query, safe='')
        full_filename = f"{base_filename}_{query_encoded}.jpg"
    else:
        full_filename = f"{base_filename}.jpg"

    return full_filename

def download_image(url, folder):
    try:
        # Get the image content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Create a filename
        filename = create_filename(url)
        
        # Create the output folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)
        
        # Save the image
        with open(os.path.join(folder, filename), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}. Reason: {e}")

def download_images_from_file(txt_file, folder):
    # Read the links from the text file
    with open(txt_file, 'r') as file:
        links = file.readlines()

    # Download each image
    for link in links:
        link = link.strip()  # Remove any surrounding whitespace
        if link:  # Ensure the link is not empty
            download_image(link, folder)

# Example usage
txt_file_path = 'dhd_links.txt'  # Change this to your text file path
output_folder = 'downloaded_images'  # Folder where images will be saved

download_images_from_file(txt_file_path, output_folder)
