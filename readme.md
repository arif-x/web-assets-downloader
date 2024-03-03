# Web Assets Downloader
## _A package for downloading web content and assets_

### Installation
run `pip3 install web-assets-downloader`

### Usage Example
```
import web_assets_downloader

urls = ['https://example.com']
save_folder = './path/to/save/folder'

web_assets_downloader.download_html_and_asset(urls, save_folder)
```