# you need to make a folder named ``Archive`` in the same directory as this file
# This script will move all the folders in the base directory to the Archive folder if they have not been modified in the last 4 weeks
# You can change the base directory and the archive directory by setting the environment variables BASE_DIR and ARCHIVE_DIR

import os
import shutil
import time
from dotenv import load_dotenv
import logging
from colorama import Fore, Style, init
import sys

# Initialize colorama
init()

# Version number
VERSION = "0.1A"

# Setup colorful logging to console
class ColorfulLogger(logging.StreamHandler):
    def emit(self, record):
        log_color = {
            'INFO': Fore.GREEN,
            'WARNING': Fore.YELLOW,
            'ERROR': Fore.RED,
            'CRITICAL': Fore.RED + Style.BRIGHT,
        }.get(record.levelname, Fore.WHITE)
        msg = self.format(record)
        self.stream.write(log_color + msg + Style.RESET_ALL + '\n')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = ColorfulLogger()
console_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))
logger.addHandler(console_handler)

load_dotenv()

base_dir = os.getenv('BASE_DIR', "C:\\Development")
archive_dir = os.getenv('ARCHIVE_DIR', os.path.join(base_dir, "Archive"))
archive_after = int(os.getenv('ARCHIVE_AFTER_SECONDS', 4 * 7 * 24 * 60 * 60))  # Defaults to 4 weeks

def archive_old_projects(directory):
    for project in os.listdir(directory):
        project_path = os.path.join(directory, project)
        if project == "Archive" or not os.path.isdir(project_path):
            continue
        last_mod_time = os.path.getmtime(project_path)
        if time.time() - last_mod_time > archive_after:
            archive_path = os.path.join(archive_dir, project)
            shutil.move(project_path, archive_path)
            logging.info(f"Archived: {project}")

def main():
    start_time = time.time()
    logging.info(f"AutoArchiver version {VERSION} started.")
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        logging.info(f"Running for {elapsed_time:.2f} seconds.")
        archive_old_projects(base_dir)
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Archiving interrupted by user.")


