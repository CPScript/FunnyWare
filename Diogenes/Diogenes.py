import os
import time
from pathlib import Path
import ctypes

# Function to restore files from the Recycle Bin
def restore_files_from_recycle_bin():
    try:
        SHEmptyRecycleBin(None, None, 0)  # Empty the Recycle Bin (optional)
    except Exception as e:
        print("Error emptying Recycle Bin:", e)
    
    desktop_path = str(Path.home() / "Desktop")
    files_to_restore = []

    # List files on the desktop that are in the Recycle Bin
    for file in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file)
        if Path(file_path).resolve().drive == Path(file_path).drive:  # Exclude files from other drives
            files_to_restore.append(file_path)

    # Restore the files from the Recycle Bin
    for file_path in files_to_restore:
        try:
            os.rename(file_path, os.path.join(desktop_path, os.path.basename(file_path)))
            print(f"Restored: {file_path}")
        except Exception as e:
            print(f"Failed to restore {file_path}: {e}")

# Load Windows API functions
SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW

# Main loop
while True:
    restore_files_from_recycle_bin()
    time.sleep(600)  # Sleep for 10 minutes (600 seconds)
