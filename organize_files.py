import os
import shutil


destination = {
    "documents": ['.txt', '.doc', '.docx', '.pdf', '.xlsx', '.pptx', '.ods', '.PDF', '.xls', 'csv'],
    "images": ['.png', '.jpg', '.jpeg', '.gif', 'heic'],
    "videos": ['.mp4'],
    "torrents": ['.torrent'],
    "applications": ['.exe', '.msi'],
    "archives": ['.zip', '.rar', '.tar', '.7zip']
}

def folder_sorter(download_path):
    print("Starting to sort folder...")
    for file in os.listdir(download_path):
        file_path = os.path.join(download_path, file)
        if os.path.isfile(file_path):
            for folder, extensions in destination.items():
                if file.endswith(tuple(extensions)):
                    folder_path = os.path.join(download_path, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    try:
                        shutil.move(file_path, folder_path)
                    except Exception as e:
                        print(f"{e} in the folder")
    print("Folder sorted")
    input("\nPress any key to continue...")

download_path = input("Enter the path here: ")
folder_sorter(download_path)