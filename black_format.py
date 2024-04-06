import subprocess
from pathlib import Path

def format_directory_with_black(directory_path):
    # Convert the directory path to a Path object to easily navigate the file system
    directory = Path(directory_path)
    
    # Check if the provided directory path exists and is indeed a directory
    if not directory.is_dir():
        print(f"The path {directory_path} is not a directory or does not exist.")
        return
    
    # Use rglob to find all .py files in the directory and its subdirectories
    python_files = directory.rglob("*.py")
    
    # Iterate through each Python file and format it with black
    for file_path in python_files:
        # Convert the file path to a string and pass it to the black command
        subprocess.run(["black", str(file_path)], check=True)
        print(f"Formatted {file_path}")

# Example usage
if __name__ == "__main__":
    directory_to_format = "C:/Users/floes/OneDrive/Dokumente/development/CS50P/problem_sets"
    format_directory_with_black(directory_to_format)