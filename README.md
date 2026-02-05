# Image Downloader

A fast, automated Python script for bulk image downloads with parallel processing and resume capability.

## Features

- 🚀 **Fast parallel downloads** (20 concurrent threads)
- ⏭️ **Skip existing files** - resume interrupted downloads
- 📊 **Progress tracking** with clear status indicators
- ⏱️ **Download timer** for performance monitoring
- 🔧 **Configurable range** and URL patterns

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install requests
   ```

2. **Run the script:**
   ```bash
   python download_images_fast.py
   ```

3. **Images are saved** in the `images/` folder

## Configuration

Edit these variables in `download_images_fast.py`:

```python
# Download range
start = 3000
end = 4000

# Skip existing files (True) or override (False)
skip_existing = True

# URL pattern
base_url = "https://example.com/path/{}_0.jpg"
```

## Status Indicators

- ✅ Downloaded successfully
- ❌ Image not found (404)
- ⚠️ Network/server error
- ⏭️ Skipped (already exists)

## Performance

- **Sequential:** ~1-2 images/second
- **Parallel (this script):** ~10-20 images/second
- **995 images:** ~1-2 minutes total

## Web Interface

A modern web UI is also available for interactive downloads:

```bash
python web_downloader.py
```

Then open `http://localhost:8000` in your browser.

## Requirements

- Python 3.6+
- `requests` library
- Internet connection
