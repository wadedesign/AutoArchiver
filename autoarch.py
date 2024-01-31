# you need to make a folder named ``Archive`` in the same directory as this file
# This script will move all the folders in the base directory to the Archive folder if they have not been modified in the last 4 weeks
# You can change the base directory and the archive directory by setting the environment variables BASE_DIR and ARCHIVE_DIR

import os
import shutil
import time
from dotenv import load_dotenv

load_dotenv()

base_dir = os.getenv('BASE_DIR', "C:\\Development")
archive_dir = os.getenv('ARCHIVE_DIR', os.path.join(base_dir, "Archive"))

# Get the current time
current_time = time.time()

# Define the period after which files should be archived, from environment variables
archive_after = int(os.getenv('ARCHIVE_AFTER_SECONDS', 4 * 7 * 24 * 60 * 60))  # Defaults to 4 weeks

# Function to archive old projects
def archive_old_projects(directory):
    for project in os.listdir(directory):
        project_path = os.path.join(directory, project)
        # Exclude the Archive directory and any non-directory files
        if project == "Archive" or not os.path.isdir(project_path):
            continue
        last_mod_time = os.path.getmtime(project_path)
        if current_time - last_mod_time > archive_after:
            archive_path = os.path.join(archive_dir, os.path.basename(project_path))
            shutil.move(project_path, archive_path)
            print(f"Archived: {project}")

archive_old_projects(base_dir)

print("Archiving complete.")

