import os
import requests
import urllib.parse

def create_filename(url):
    
    parsed_url = urllib.parse.urlparse(url)
    
    
    path = parsed_url.path
    query = parsed_url.query
    
    
    base_filename = os.path.basename(path)  
    if query:  
        query_encoded = urllib.parse.quote(query, safe='')
        full_filename = f"{base_filename}_{query_encoded}.jpg"
    else:
        full_filename = f"{base_filename}.jpg"

    return full_filename

def download_image(url, folder):
    try:
        
        response = requests.get(url)
        response.raise_for_status()  
        
        
        filename = create_filename(url)
        
        
        os.makedirs(folder, exist_ok=True)
        
        
        with open(os.path.join(folder, filename), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}. Reason: {e}")

def download_images_from_file(txt_file, folder):
    
    with open(txt_file, 'r') as file:
        links = file.readlines()

    
    for link in links:
        link = link.strip()  
        if link:  
            download_image(link, folder)


txt_file_path = 'dhd_links.txt'  
output_folder = 'downloaded_images'  

download_images_from_file(txt_file_path, output_folder)
