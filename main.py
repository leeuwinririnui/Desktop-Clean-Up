import customtkinter
import shutil
import os

# source directory
source_dir = "C:\\Users\\leeuw\\OneDrive\\Desktop"

# for adjusting appearance mode (light and dark)
options = ["Light", "Dark"]

# app will be in dark mode by default
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Desktop Cleaner")
root.geometry("350x350")


# function to clean up files
def delete():
    file_extension = entry_file_type.get()
    for filename in os.listdir(source_dir):
        # get path of file
        file_path = os.path.join(source_dir, filename)

        # check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # split the filename and extension
            base_name, extension = os.path.splitext(filename)

            # check if the extension needs to be deleted
            if extension.lower() == '.' + file_extension.lower():
                # delete the file
                try:
                    # Delete the file
                    os.remove(file_path)
                    label_msg.configure(text="deletion successful!")
                    print(f"Deleted: {filename}")
                except OSError as e:
                    # insert error text for user
                    label_msg.configure(text="error deleting files...")
                    print(f"Error deleting {filename}: {e}")


# function to clean up files but organising categorize folders based on file extension
def clean_up():
    file_extension = entry_file_type.get()
    for filename in os.listdir(source_dir):
        # get file path
        file_path = os.path.join(source_dir, filename)
        # check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # split the filename and extension
            base_name, extension = os.path.splitext(filename)
            # check if extension needs to be cleaned up
            if extension.lower() == '.' + file_extension.lower():
                # new path for folder
                folder_path = "C:\\Users\\leeuw\\OneDrive\\Desktop\\" + file_extension
                # if path does not exist create new folder
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # move files of compatible type into folder
                source = os.path.join(source_dir, filename)
                destination = os.path.join(folder_path, filename)
                shutil.move(source, destination)
                # confirmation
                print(f"Folder '{folder_path}' files cleaned")
                label_msg.configure(text="Files cleaned")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=12, padx=10, fill="both", expand=True)

label_title = customtkinter.CTkLabel(master=frame, text="Desktop Cleaner", font=("Roboto", 16, "bold"))
label_title.pack(pady=12, padx=10)

entry_file_type = customtkinter.CTkEntry(master=frame, placeholder_text="File Type")
entry_file_type.pack(pady=12, padx=10)

button_clean = customtkinter.CTkButton(master=frame, text="Clean Up", command=clean_up)
button_clean.pack(pady=12, padx=10)

button_clean_all = customtkinter.CTkButton(master=frame, text="Clean All")
button_clean_all.pack(pady=12, padx=10)

button_delete = customtkinter.CTkButton(master=frame, text="Delete", command=delete)
button_delete.pack(pady=12, padx=10)

label_msg = customtkinter.CTkLabel(master=frame, text="")
label_msg.pack(pady=4, padx=3)

root.mainloop()
