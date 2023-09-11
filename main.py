import os


directory_path = '<your/directory/path/goes/here>' #using "/" instead of "\" is recommended
if os.path.isdir(directory_path):
    folder_names = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]
    print("Folder names in the specified directory:")
    for folder_name in folder_names:
        print(folder_name)
else:
    print("The specified path is not a directory.")