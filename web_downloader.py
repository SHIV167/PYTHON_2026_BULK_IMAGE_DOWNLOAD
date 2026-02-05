import os
import requests
from flask import Flask, render_template, request, jsonify, send_file
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from urllib.parse import urlparse
import threading

app = Flask(__name__)

# Global variables for download status
download_status = {"running": False, "progress": [], "completed": 0, "total": 0}

def download_image(url, filename, index):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open(filename, "wb") as f:
                f.write(r.content)
            return {"index": index, "status": "success", "message": f"✅ Downloaded {index}"}
        else:
            return {"index": index, "status": "error", "message": f"❌ Not found: {index}"}
    except Exception as e:
        return {"index": index, "status": "error", "message": f"⚠️ Error at {index}: {str(e)}"}

def batch_download(base_url, start, end, folder, skip_existing):
    global download_status
    download_status = {"running": True, "progress": [], "completed": 0, "total": end - start + 1}
    
    os.makedirs(folder, exist_ok=True)
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        
        for i in range(start, end + 1):
            url = base_url.format(i)
            filename = os.path.join(folder, f"{i}_0.jpg")
            
            if skip_existing and os.path.exists(filename):
                download_status["progress"].append({"index": i, "status": "skipped", "message": f"⏭️ Skipped {i}"})
                download_status["completed"] += 1
                continue
            
            future = executor.submit(download_image, url, filename, i)
            futures.append(future)
        
        for future in as_completed(futures):
            result = future.result()
            download_status["progress"].append(result)
            download_status["completed"] += 1
    
    download_status["running"] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def start_download():
    data = request.json
    base_url = data['base_url']
    start = int(data['start'])
    end = int(data['end'])
    folder = data['folder']
    skip_existing = data.get('skip_existing', True)
    
    # Start download in background thread
    thread = threading.Thread(target=batch_download, args=(base_url, start, end, folder, skip_existing))
    thread.start()
    
    return jsonify({"status": "started", "total": end - start + 1})

@app.route('/status')
def get_status():
    return jsonify(download_status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
