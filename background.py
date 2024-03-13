import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
import shutil
import os

# source directory
source_dir = "C:\\Users\\leeuw\\OneDrive\\Desktop"

extension_audio = ['wav', 'mp3', 'raw', 'mid', 'wma', 'midi', 'm4a']
extension_compress = ['zip', '7z', 'z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
extension_install = ['dmg', 'exe', 'iso']
extension_image = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif', 'ico']
extension_video = ['mp4', 'mpg', 'mpeg', 'mov', 'avi', 'flv', 'mkv', 'mwv', 'm4v', 'h264']
extension_docs = ['txt', 'accdb', 'pdf', 'rtf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt',
                  'pptx', 'log']


# retrieve file type based on extension
def retrieve_type(extension):
    for ext in extension_docs:
        if "." + ext.lower() == extension.lower():  # condition isn't being met
            return "Documents"
    for ext in extension_audio:
        if "." + ext.lower() == extension.lower():  # condition isn't being met
            return "Audio"
    for ext in extension_video:
        if "." + ext.lower() == extension.lower():  # condition isn't being met
            return "Videos"
    for ext in extension_image:
        if "." + ext.lower() == extension.lower():  # condition isn't being met
            return "Pictures"
    for ext in extension_install:
        if "." + ext.lower() == extension.lower():  # condition isn't being met
            return "Applications"
    for ext in extension_compress:
        if "." + ext.lower() == extension.lower():  # condition isn't being met
            return "Zip"


# retrieve extension based on file type
def retrieve_extension(file_type):
    if file_type == "Documents":
        return extension_docs
    elif file_type == "Audio":
        return extension_audio
    elif file_type == "Pictures":
        return extension_image
    elif file_type == "Videos":
        return extension_video
    elif file_type == "Applications":
        return extension_install


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # begin iteration through files to sort
        for filename in os.listdir(source_dir):
            # get file path
            file_path = os.path.join(source_dir, filename)
            # check if it's a file (not a directory)
            if os.path.isfile(file_path):
                # split the filename and extension
                base_name, extension = os.path.splitext(filename)

                file_type = retrieve_type(extension)

                folder_path = source_dir + "\\" + file_type
                # if path does not exist create new folder
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # move files of compatible type into folder
                source = os.path.join(source_dir, filename)
                destination = os.path.join(folder_path, filename)
                shutil.move(source, destination)
                print(f"Folder '{folder_path}' files cleaned")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
