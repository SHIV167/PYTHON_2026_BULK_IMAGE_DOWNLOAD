import os
import shutil

def organize_by_ranges(source_folder="images", range_size=500):
    """Simple organization by number ranges"""
    
    output_folder = "organized_images"
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all image files
    image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]
    
    # Extract numbers and sort
    numbered_files = []
    for f in image_files:
        try:
            num = int(f.split('_')[0])
            numbered_files.append((num, f))
        except:
            continue
    
    numbered_files.sort()
    
    if not numbered_files:
        print("No valid image files found!")
        return
    
    min_num = numbered_files[0][0]
    max_num = numbered_files[-1][0]
    
    print(f"Found {len(numbered_files)} images")
    print(f"Organizing from {min_num} to {max_num} in ranges of {range_size}")
    
    # Create folders and copy files
    for start in range(min_num, max_num + 1, range_size):
        end = min(start + range_size - 1, max_num)
        folder_name = f"batch_{start:04d}_{end:04d}"
        folder_path = os.path.join(output_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        count = 0
        for num, filename in numbered_files:
            if start <= num <= end:
                src_path = os.path.join(source_folder, filename)
                dst_path = os.path.join(folder_path, filename)
                shutil.copy2(src_path, dst_path)
                count += 1
        
        print(f"✅ {folder_name}: {count} images")
    
    print(f"\n🎉 Organization complete! Images saved to '{output_folder}' folder")

if __name__ == "__main__":
    print("📁 Simple Image Organizer")
    print("=" * 30)
    
    # You can change the range size here
    organize_by_ranges(range_size=500)
