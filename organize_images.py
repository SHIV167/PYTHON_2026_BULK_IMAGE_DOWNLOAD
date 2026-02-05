import os
import shutil
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import cv2
import json

def get_image_features(image_path):
    """Extract features from image for clustering"""
    try:
        # Read image
        img = cv2.imread(image_path)
        if img is None:
            return None
        
        # Resize for consistent processing
        img = cv2.resize(img, (100, 100))
        
        # Convert to RGB and flatten
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        features = img_rgb.flatten()
        
        # Add color histogram features
        hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = hist.flatten()
        
        # Combine features
        combined_features = np.concatenate([features, hist])
        
        return combined_features
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def organize_images_by_similarity(source_folder, output_folder, num_clusters=10):
    """Organize images into folders based on visual similarity"""
    
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all image files
    image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]
    print(f"Found {len(image_files)} images")
    
    # Extract features
    features = []
    valid_files = []
    
    print("Extracting features from images...")
    for i, img_file in enumerate(image_files):
        if i % 100 == 0:
            print(f"Processing {i}/{len(image_files)}")
        
        img_path = os.path.join(source_folder, img_file)
        feature = get_image_features(img_path)
        
        if feature is not None:
            features.append(feature)
            valid_files.append(img_file)
    
    if not features:
        print("No valid images found!")
        return
    
    # Convert to numpy array
    features = np.array(features)
    
    # Apply K-means clustering
    print(f"Clustering images into {num_clusters} groups...")
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(features)
    
    # Create folders for each cluster
    for i in range(num_clusters):
        cluster_folder = os.path.join(output_folder, f"cluster_{i+1:02d}")
        os.makedirs(cluster_folder, exist_ok=True)
    
    # Move images to their respective folders
    print("Organizing images into folders...")
    for i, (img_file, cluster) in enumerate(zip(valid_files, cluster_labels)):
        src_path = os.path.join(source_folder, img_file)
        dst_folder = os.path.join(output_folder, f"cluster_{cluster+1:02d}")
        dst_path = os.path.join(dst_folder, img_file)
        
        # Copy file (use copy instead of move to be safe)
        shutil.copy2(src_path, dst_path)
        
        if (i + 1) % 100 == 0:
            print(f"Organized {i+1}/{len(valid_files)} images")
    
    # Save cluster information
    cluster_info = {}
    for i, (img_file, cluster) in enumerate(zip(valid_files, cluster_labels)):
        cluster_name = f"cluster_{cluster+1:02d}"
        if cluster_name not in cluster_info:
            cluster_info[cluster_name] = []
        cluster_info[cluster_name].append(img_file)
    
    with open(os.path.join(output_folder, 'cluster_info.json'), 'w') as f:
        json.dump(cluster_info, f, indent=2)
    
    print(f"\n✅ Organization complete!")
    print(f"Created {num_clusters} folders in '{output_folder}'")
    print(f"Cluster information saved to 'cluster_info.json'")
    
    # Print summary
    for cluster_name, files in cluster_info.items():
        print(f"{cluster_name}: {len(files)} images")

def organize_by_number_ranges(source_folder, output_folder, range_size=500):
    """Organize images by number ranges (e.g., 1-500, 501-1000)"""
    
    os.makedirs(output_folder, exist_ok=True)
    
    image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]
    
    # Extract numbers from filenames
    numbers = []
    for f in image_files:
        try:
            num = int(f.split('_')[0])
            numbers.append((num, f))
        except:
            continue
    
    # Sort by number
    numbers.sort()
    
    # Create ranges
    if not numbers:
        print("No valid image files found!")
        return
    
    min_num = numbers[0][0]
    max_num = numbers[-1][0]
    
    print(f"Organizing images from {min_num} to {max_num}")
    
    for start in range(min_num, max_num + 1, range_size):
        end = min(start + range_size - 1, max_num)
        folder_name = f"images_{start}_{end}"
        folder_path = os.path.join(output_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        # Copy images in this range
        for num, filename in numbers:
            if start <= num <= end:
                src_path = os.path.join(source_folder, filename)
                dst_path = os.path.join(folder_path, filename)
                shutil.copy2(src_path, dst_path)
        
        print(f"Created {folder_name} with images {start}-{end}")

if __name__ == "__main__":
    source_folder = "images"
    
    print("Image Organization Options:")
    print("1. Organize by visual similarity (AI clustering)")
    print("2. Organize by number ranges")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        output_folder = "organized_by_similarity"
        num_clusters = int(input("Number of clusters (default 10): ") or "10")
        
        print("\n⚠️  This requires additional packages: scikit-learn, opencv-python")
        install = input("Install required packages? (y/n): ").strip().lower()
        
        if install == 'y':
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-learn", "opencv-python", "Pillow"])
        
        organize_images_by_similarity(source_folder, output_folder, num_clusters)
        
    elif choice == "2":
        output_folder = "organized_by_ranges"
        range_size = int(input("Range size (default 500): ") or "500")
        organize_by_number_ranges(source_folder, output_folder, range_size)
        
    else:
        print("Invalid choice!")
