# you need to make a folder named ``Archive`` in the same directory as this file
# This script will move all the folders in the base directory to the Archive folder if they have not been modified in the last 4 weeks
# You can change the base directory and the archive directory by setting the environment variables BASE_DIR and ARCHIVE_DIR

import os
import shutil
import time
import logging
from colorama import Fore, Style, init
import argparse
from config import BASE_DIR, ARCHIVE_DIR, ARCHIVE_AFTER_SECONDS, VERSION
from utils import progress_bar, should_include_file, should_exclude_dir

init()

class ColorfulLogger(logging.StreamHandler):
    def emit(self, record):
        log_color = {
            'INFO': Fore.GREEN,
            'WARNING': Fore.YELLOW,
            'ERROR': Fore.RED,
            'CRITICAL': Fore.RED + Style.BRIGHT,
        }.get(record.levelname, Fore.WHITE)
        emoji = {
            'INFO': 'ℹ️ ',
            'WARNING': '⚠️ ',
            'ERROR': '❌ ',
            'CRITICAL': '🔥 ',
        }.get(record.levelname, '🔷 ')
        msg = self.format(record)
        self.stream.write(log_color + emoji + msg + Style.RESET_ALL + '\n')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = ColorfulLogger()
console_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))
logger.addHandler(console_handler)

def archive_old_projects(directory, include_types, exclude_types, exclude_dirs, archive_after, archive_dir):
    file_count = sum([len(files) for _, _, files in os.walk(directory)])
    processed = 0
    for root, dirs, files in os.walk(directory, topdown=True):
        dirs[:] = [d for d in dirs if not should_exclude_dir(os.path.join(root, d), exclude_dirs)]
        for file in files:
            if not should_include_file(file, include_types, exclude_types):
                continue
            file_path = os.path.join(root, file)
            last_mod_time = os.path.getmtime(file_path)
            if time.time() - last_mod_time > archive_after:
                archive_path = os.path.join(archive_dir, os.path.relpath(root, directory), file)
                os.makedirs(os.path.dirname(archive_path), exist_ok=True)
                shutil.move(file_path, archive_path)
                logging.info(f"📦 Archived: {file_path}")
            processed += 1

            
total = 100
for i in range(0, total + 1):
    print(progress_bar(i, total), end='\r')
    time.sleep(0.05)


def main():
    parser = argparse.ArgumentParser(description="📦 AutoArchiver with configurable file selection")
    parser.add_argument("--base-dir", default=BASE_DIR, help="Base directory to scan 📁")
    parser.add_argument("--archive-dir", default=ARCHIVE_DIR, help="Directory to archive old projects 🗄️")
    parser.add_argument("--archive-after", type=int, default=ARCHIVE_AFTER_SECONDS, help="Archive files older than this duration (in seconds) ⏳")
    parser.add_argument("--include-types", nargs="*", help="List of file extensions to include in archive 📄")
    parser.add_argument("--exclude-types", nargs="*", help="List of file extensions to exclude from archive ❌")
    parser.add_argument("--exclude-dirs", nargs="*", help="List of directories to exclude from archive 🚫")
    args = parser.parse_args()

    start_time = time.time()
    logging.info("AutoArchiver version " + VERSION + " started.")
    if not args.archive_dir:
        args.archive_dir = os.path.join(args.base_dir, "Archive")
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        logging.info(f"⏰ Running for {elapsed_time:.2f} seconds.")
        archive_old_projects(args.base_dir, args.include_types, args.exclude_types, args.exclude_dirs or [], args.archive_after, args.archive_dir)
        time.sleep(60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("🛑 Archiving interrupted by user.")





