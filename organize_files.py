import os
import shutil


destination = {
    "documents": ['.txt', '.doc', '.docx', '.pdf', 'xlsx', 'pptx', 'ods'],
    "images": ['.png', '.jpg', '.jpeg', '.gif', 'heic'],
    "videos": ['.mp4'],
    "torrents": ['.torrent'],
    "applications": ['.exe'],
    "archives": ['.zip', '.rar', '.tar', '.7zip']
}

def folder_sorter(download_path):
    for file in os.listdir(download_path):
        file_path = os.path.join(download_path, file)
        if os.path.isfile(file_path):
            for folder, extensions in destination.items():
                if file.endswith(tuple(extensions)):
                    folder_path = os.path.join(download_path, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, folder_path)
    print("Folder sorted")

download_path = input("Enter the path here: ")
folder_sorter(download_path)