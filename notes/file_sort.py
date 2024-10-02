import os
import shutil

# Define the path to the Downloads directory
downloads_dir = os.path.expanduser('~/Downloads')

# Define where the files should go based on their extensions
file_types = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".ogg"],
    "Programs": [".exe", ".msi", ".dmg", ".pkg", ".sh"],
}

# Create folders if they don't exist
def create_folders(base_dir):
    for folder in file_types.keys():
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Function to move files to corresponding folders
def sort_files(base_dir):
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)

        # Only process files, skip directories
        if os.path.isfile(item_path):
            file_ext = os.path.splitext(item)[1].lower()
            moved = False

            # Check which category the file belongs to based on its extension
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(item_path, os.path.join(base_dir, folder, item))
                    print(f"Moved: {item} to {folder}")
                    moved = True
                    break

            # Move to 'Other' folder if extension doesn't match any category
            if not moved:
                other_folder = os.path.join(base_dir, "Other")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(item_path, os.path.join(other_folder, item))
                print(f"Moved: {item} to Other")

if __name__ == "__main__":
    # Create necessary folders
    create_folders(downloads_dir)

    # Sort the files in the Downloads folder
    sort_files(downloads_dir)