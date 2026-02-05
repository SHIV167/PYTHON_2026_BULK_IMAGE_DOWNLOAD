import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Folder to save images
folder = "images"
os.makedirs(folder, exist_ok=True)

base_url = "https://duuvt8uneo2c1.cloudfront.net/media/public/large/{}_0.jpg"

start = 2000
end = 3000

# Options
skip_existing = True  # Set to False to override existing files

def download_image(i):
    url = base_url.format(i)
    filename = os.path.join(folder, f"{i}_0.jpg")
    
    # Check if file exists and skip option is enabled
    if skip_existing and os.path.exists(filename):
        return f"⏭️ Skipped {i} (already exists)"
    
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            with open(filename, "wb") as f:
                f.write(r.content)
            return f"✅ Downloaded {i}"
        else:
            return f"❌ Not found: {i}"
    except Exception as e:
        return f"⚠️ Error at {i}: {e}"

print(f"🚀 Starting fast download of {end - start + 1} images...")
start_time = time.time()

# Use ThreadPoolExecutor for parallel downloads (20 threads)
with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(download_image, i) for i in range(start, end + 1)]
    
    for future in as_completed(futures):
        print(future.result())

end_time = time.time()
print(f"⏱️ Completed in {end_time - start_time:.2f} seconds")
