# Image Downloader & Organizer

A comprehensive Python toolkit for bulk image downloads with parallel processing, resume capability, and intelligent organization by visual similarity.

## Features

### 📥 **Download Capabilities**
- 🚀 **Fast parallel downloads** (20 concurrent threads)
- ⏭️ **Skip existing files** - resume interrupted downloads
- 📊 **Progress tracking** with clear status indicators
- ⏱️ **Download timer** for performance monitoring
- 🔧 **Configurable range** and URL patterns

### 🗂️ **Organization Tools**
- 🤖 **AI-powered clustering** - groups images by visual similarity
- 📁 **Range-based organization** - organize by number ranges
- 📋 **Smart categorization** - automatic subject grouping
- 📊 **Cluster analysis** - detailed grouping statistics

## Quick Start

### 📥 **Download Images**

1. **Install basic dependencies:**
   ```bash
   pip install requests
   ```

2. **Run the fast downloader:**
   ```bash
   python download_images_fast.py
   ```

3. **Images are saved** in the `images/` folder

### 🗂️ **Organize Images**

#### **Simple Organization (Recommended)**
```bash
python simple_organize.py
```
Creates organized folders by number ranges (e.g., batch_0001_0500/)

#### **AI-Powered Organization**
```bash
# Install AI dependencies first
pip install scikit-learn opencv-python Pillow scipy numpy joblib

# Run smart organizer
python organize_images.py
```
Groups images by visual similarity using machine learning

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

## 📈 **Status Indicators**

- ✅ Downloaded successfully
- ❌ Image not found (404)
- ⚠️ Network/server error
- ⏭️ Skipped (already exists)

## 🌐 **Web Interface**

A modern web UI is available for interactive downloads:

```bash
# Install Flask first
pip install flask

# Run web server
python web_downloader.py
```

Then open `http://localhost:8000` in your browser.

**Features:**
- Interactive URL pattern input
- Real-time progress tracking
- Download range configuration
- Modern responsive UI

## 📊 **Organization Results**

### **Simple Organization Example**
```
organized_images/
├── batch_0001_0500/    (500 images)
├── batch_0501_1000/    (500 images)
├── batch_1001_1500/    (498 images)
└── ...
```

### **AI Clustering Example**
```
organized_by_similarity/
├── cluster_01/          (982 images - similar visual theme)
├── cluster_07/          (1345 images - main subject)
├── cluster_10/          (476 images)
└── cluster_info.json    (detailed mapping)
```

## 🛠️ **Advanced Configuration**

### **Download Settings**
```python
# download_images_fast.py
start = 3000
end = 4000
skip_existing = True
base_url = "https://example.com/path/{}_0.jpg"
```

### **Organization Settings**
```python
# simple_organize.py
range_size = 500  # Images per folder

# organize_images.py
num_clusters = 10  # Number of visual groups
```

## 📋 **Requirements**

### **Basic (Download + Simple Organize)**
- Python 3.6+
- `requests` library
- Internet connection

### **AI Organization**
- All basic requirements
- `scikit-learn` - machine learning clustering
- `opencv-python` - image processing
- `Pillow` - image handling
- `scipy` - scientific computing
- `numpy` - numerical operations
- `joblib` - parallel processing

### **Web Interface**
- All basic requirements
- `flask` - web framework

## 🚀 **Performance**

- **Sequential downloads:** ~1-2 images/second
- **Parallel downloads:** ~10-20 images/second
- **995 images:** ~1-2 minutes total
- **AI clustering:** ~2-5 minutes for 4000+ images
- **Simple organization:** ~10-30 seconds

---

## 📁 **File Structure**

```
IMAGE_FORMAT/
├── download_images.py           # Basic downloader
├── download_images_fast.py      # Fast parallel downloader
├── simple_organize.py          # Range-based organizer
├── organize_images.py          # AI-powered organizer
├── web_downloader.py           # Web interface
├── templates/
│   └── index.html             # Web UI template
├── images/                    # Downloaded images
├── organized_images/          # Range-based organization
├── organized_by_similarity/   # AI clustering results
└── README.md                  # This file
```

## 🎯 **Use Cases**

- **Research:** Bulk download academic image datasets
- **Data Collection:** Gather images for machine learning projects
- **Content Management:** Organize large image libraries
- **Batch Processing:** Prepare images for analysis workflows
- **Web Scraping:** Download image sequences from websites

## 🤝 **Contributing**

Feel free to improve the toolkit:
1. Add new organization algorithms
2. Enhance the web interface
3. Optimize download performance
4. Add more image format support

## 📄 **License**

This project is open source and available under the MIT License.
