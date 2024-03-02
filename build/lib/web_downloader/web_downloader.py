import os
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote

def download_asset(asset_urls, save_folder, headers):
    for url in asset_urls:
        print(url)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Parse the asset URL to extract the path
            parsed_url = urlparse(url)
            asset_path = unquote(parsed_url.path)

            # Construct the filepath within the assets directory
            asset_filepath = os.path.join(save_folder, asset_path.lstrip('/'))

            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(asset_filepath), exist_ok=True)

            # Download the asset
            with open(asset_filepath, 'wb') as f:
                f.write(response.content)
                print(f"Downloaded {asset_path}.")

def download_html_and_asset(url_list, save_folder):
    # Standard User-Agent header for a common web browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    for url in url_list:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            base_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}"

            # Extract the filename from the last part of the URL path
            filename = os.path.basename(urlparse(url).path)
            if not filename:
                filename = "index.html"

            # Save HTML content
            html_filepath = os.path.join(save_folder, filename)

            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(html_filepath), exist_ok=True)

            with open(html_filepath, 'wb') as f:
                f.write(response.content)
                print(f"HTML content saved for {url} as {filename}.")

            # Extract asset URLs
            asset_urls = set()
            for tag in soup.find_all(['img', 'link', 'script']):
                if tag.has_attr('src'):
                    asset_url = tag['src']
                elif tag.has_attr('href'):
                    asset_url = tag['href']
                else:
                    continue

                absolute_url = urljoin(base_url, asset_url)

                print(absolute_url)
                asset_urls.add(absolute_url)

            # Download assets
            download_asset(asset_urls, save_folder, headers)

    return True
