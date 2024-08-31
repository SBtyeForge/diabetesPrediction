import os
import sys
import shutil
import zipfile

def unzip_and_move(zip_file, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Unzip the file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

    # Get the extracted folder name
    extracted_folder = os.path.splitext(os.path.basename(zip_file))[0]

    # Move the contents to the destination folder
    source_folder = os.path.join(destination_folder, extracted_folder)
    for item in os.listdir(source_folder):
        source = os.path.join(source_folder, item)
        destination = os.path.join(destination_folder, item)
        if os.path.isdir(source):
            shutil.move(source, destination)
        else:
            shutil.move(source, destination_folder)

    # Remove the extracted folder
    os.rmdir(source_folder)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python unzip_and_move.py <zip_file> <destination_folder>")
        sys.exit(1)

    zip_file = sys.argv[1]
    destination_folder = sys.argv[2]

    unzip_and_move(zip_file, destination_folder)
