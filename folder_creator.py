import os
import sys
import shutil

def create_folders_and_move_py_files(directory):
    """
    Creates a folder for each .py file in the given directory and moves the .py file into its corresponding folder.
    The folder will have the same name as the .py file, without the extension.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the current file is a .py file
        if filename.endswith('.py'):
            # Construct the folder name by removing the .py extension
            folder_name = os.path.splitext(filename)[0]
            # Construct the full path for the new folder
            folder_path = os.path.join(directory, folder_name)
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Folder created: {folder_path}")
            else:
                print(f"Folder already exists: {folder_path}")
            
            # Construct the full path of the current file
            file_path = os.path.join(directory, filename)
            # Construct the new path for the file inside its folder
            new_file_path = os.path.join(folder_path, filename)
            # Move the file to the new folder
            shutil.move(file_path, new_file_path)
            print(f"Moved {filename} to {new_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python folder_creator.py <directory>")
    else:
        directory = sys.argv[1]
        create_folders_and_move_py_files(directory)