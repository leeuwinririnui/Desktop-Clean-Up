import customtkinter
import shutil
import os
import tkinter.messagebox as messagebox

# file extensions
extension_audio = ['wav', 'mp3', 'raw', 'mid', 'wma', 'midi', 'm4a']
extension_compress = ['zip', '7z', 'z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
extension_install = ['dmg', 'exe', 'iso']
extension_image = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif', 'ico']
extension_video = ['mp4', 'mpg', 'mpeg', 'mov', 'avi', 'flv', 'mkv', 'mwv', 'm4v', 'h264']
extension_docs = ['txt', 'accdb', 'pdf', 'rtf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt',
                  'pptx', 'log']

# source directory
source_dir = "C:\\Users\\leeuw\\OneDrive\\Desktop"

# folders for storing files
destination_dirs = ['Audio', 'Pictures', 'Documents', 'Videos', 'Applications', 'Other']

# for adjusting appearance mode (light and dark)
options = ["Light", "Dark"]

# app will be in dark mode by default
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Desktop Cleaner")
root.geometry("300x350")


# function to change appearance mode
def appearance_mode():
    if customtkinter.get_appearance_mode() == "Dark":
        customtkinter.set_appearance_mode("Light")
        customtkinter.set_default_color_theme("blue")
    else:
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")


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


# function to clean up files
def delete():
    response = messagebox.askyesno("Confirm", f"Are you sure? All {combobox_files.get().lower()} will be deleted")
    if response:
        file_type = combobox_files.get()
        file_ext = retrieve_extension(file_type)

        for filename in os.listdir(source_dir):
            # get path of file
            file_path = os.path.join(source_dir, filename)

            # check if it's a file (not a directory)
            if os.path.isfile(file_path):
                # split the filename and extension
                base_name, extension = os.path.splitext(filename)

                for file_extension in file_ext:
                    # check if the extension needs to be deleted
                    if extension.lower() == '.' + file_extension.lower():
                        # delete the file
                        try:
                            # Delete the file
                            os.remove(file_path)
                            print(f"Deleted: {filename}")
                        except OSError as e:
                            # insert error text for user
                            print(f"Error deleting {filename}: {e}")


# function to clean up files by organising folders based on file extension
def clean_up():
    # assign extensions based on file type
    file_type = combobox_files.get()
    file_ext = retrieve_extension(file_type)

    # begin iteration through files to sort
    for filename in os.listdir(source_dir):
        # get file path
        file_path = os.path.join(source_dir, filename)
        # check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # split the filename and extension
            base_name, extension = os.path.splitext(filename)
            # check if extension needs to be cleaned up
            for file_extension in file_ext:
                # print(f"{file_extension}")
                # check if extensions match
                if extension.lower() == "." + file_extension.lower():
                    # new path for folder
                    folder_path = source_dir + "\\" + file_type
                    # if path does not exist create new folder
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    # move files of compatible type into folder
                    source = os.path.join(source_dir, filename)
                    destination = os.path.join(folder_path, filename)
                    shutil.move(source, destination)
                    # confirmation
                    print(f"Folder '{folder_path}' files cleaned")


def clean_all():
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


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=12, padx=10, fill="both", expand=True)

label_title = customtkinter.CTkLabel(master=frame, text="Desktop Cleaner", font=("Roboto", 16, "bold"))
label_title.pack(pady=12, padx=10)

combobox_files = customtkinter.CTkComboBox(master=frame, values=destination_dirs)
combobox_files.pack(pady=12, padx=10)

button_clean = customtkinter.CTkButton(master=frame, text="Clean", command=clean_up)
button_clean.pack(pady=12, padx=10)

button_delete = customtkinter.CTkButton(master=frame, text="Clean All", command=clean_all)
button_delete.pack(pady=12, padx=10)

button_delete = customtkinter.CTkButton(master=frame, text="Delete", command=delete)
button_delete.pack(pady=12, padx=10)

button_appearance = customtkinter.CTkButton(master=frame, text="Appearance", command=appearance_mode)
button_appearance.pack(pady=12, padx=10)

root.mainloop()
