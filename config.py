from dotenv import load_dotenv
import os

load_dotenv()

VERSION = "0.1A 🚀"

BASE_DIR = os.getenv('BASE_DIR', "C:\\Development")
ARCHIVE_DIR = os.getenv('ARCHIVE_DIR')
ARCHIVE_AFTER_SECONDS = int(os.getenv('ARCHIVE_AFTER_SECONDS', 4 * 7 * 24 * 60 * 60))
