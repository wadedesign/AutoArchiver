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
import argparse

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

# Command line arguments
parser = argparse.ArgumentParser(description="AutoArchiver with configurable file selection")
parser.add_argument("--base-dir", default=os.getenv('BASE_DIR', "C:\\Development"), help="Base directory to scan")
parser.add_argument("--archive-dir", default=os.getenv('ARCHIVE_DIR'), help="Directory to archive old projects")
parser.add_argument("--archive-after", type=int, default=int(os.getenv('ARCHIVE_AFTER_SECONDS', 4 * 7 * 24 * 60 * 60)), help="Archive files older than this duration (in seconds)")
parser.add_argument("--include-types", nargs="*", help="List of file extensions to include in archive")
parser.add_argument("--exclude-types", nargs="*", help="List of file extensions to exclude from archive")
parser.add_argument("--exclude-dirs", nargs="*", help="List of directories to exclude from archive")
args = parser.parse_args()

def should_include_file(file, include_types, exclude_types):
    if include_types:
        return any(file.endswith(ext) for ext in include_types)
    if exclude_types:
        return not any(file.endswith(ext) for ext in exclude_types)
    return True

def should_exclude_dir(dir, exclude_dirs):
    return any(ex_dir in dir for ex_dir in exclude_dirs)

def archive_old_projects(directory, include_types, exclude_types, exclude_dirs):
    for root, dirs, files in os.walk(directory, topdown=True):
        dirs[:] = [d for d in dirs if not should_exclude_dir(os.path.join(root, d), exclude_dirs)]
        for file in files:
            if not should_include_file(file, include_types, exclude_types):
                continue
            file_path = os.path.join(root, file)
            last_mod_time = os.path.getmtime(file_path)
            if time.time() - last_mod_time > args.archive_after:
                archive_path = os.path.join(args.archive_dir, os.path.relpath(root, directory), file)
                os.makedirs(os.path.dirname(archive_path), exist_ok=True)
                shutil.move(file_path, archive_path)
                logging.info(f"Archived: {file_path}")

def main():
    start_time = time.time()
    logging.info(f"AutoArchiver version {VERSION} started.")
    if not args.archive_dir:
        args.archive_dir = os.path.join(args.base_dir, "Archive")
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        logging.info(f"Running for {elapsed_time:.2f} seconds.")
        archive_old_projects(args.base_dir, args.include_types, args.exclude_types, args.exclude_dirs or [])
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Archiving interrupted by user.")


