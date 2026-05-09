import os
import re
import urllib.request

base_url = "https://www.skyscapeholidays.in/"
files_to_parse = ["original_skyscape.html", "original_style.css", "original_script.js"]
assets = set()

for filename in files_to_parse:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            # Match assets/... something
            matches = re.findall(r'(assets/[^"\'\s)]+\.(?:webp|png|jpg|jpeg|mp4|svg|woff|woff2|ttf|ico))', content)
            for match in matches:
                assets.add(match)
            # Match places/...
            matches2 = re.findall(r'(places/[^"\'\s)]+\.(?:webp|png|jpg|jpeg|mp4|svg|woff|woff2|ttf|ico))', content)
            for match in matches2:
                assets.add(match)

print(f"Found {len(assets)} assets to download.")

for asset in assets:
    local_path = os.path.join("original_assets", asset)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    url = base_url + asset
    print(f"Downloading {asset}...")
    try:
        # User-Agent header to avoid 403 Forbidden
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
    except Exception as e:
        print(f"Failed to download {asset}: {e}")

print("Done.")
