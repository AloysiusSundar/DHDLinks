import json
import os

def extract_dhd_links(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract 'dhd' links
    dhd_links = []
    for item in data.get('data', {}).values():
        if 'dhd' in item:
            dhd_links.append(item['dhd'])
    
    return dhd_links

def save_links_to_file(links, output_file):
    with open(output_file, 'w') as file:
        for link in links:
            file.write(link + '\n')
    print(f"Links saved to {output_file}")

# Example usage:
json_file_path = 'links.json'  # Change this to the path of your file
output_txt_file = 'dhd_links.txt'  # Name of the output text file

dhd_links = extract_dhd_links(json_file_path)

if dhd_links:
    save_links_to_file(dhd_links, output_txt_file)
else:
    print("No 'dhd' links found.")
