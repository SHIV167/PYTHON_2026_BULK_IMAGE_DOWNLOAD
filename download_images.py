import os
import requests

# Folder to save images
folder = "images"
os.makedirs(folder, exist_ok=True)

base_url = "https://duuvt8uneo2c1.cloudfront.net/media/public/large/{}_0.jpg"

start = 3006
end = 4000

for i in range(start, end + 1):
    url = base_url.format(i)
    filename = os.path.join(folder, f"{i}_0.jpg")
    
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open(filename, "wb") as f:
                f.write(r.content)
            print(f"✅ Downloaded {i}")
        else:
            print(f"❌ Not found: {i}")
    except Exception as e:
        print(f"⚠️ Error at {i}: {e}")
