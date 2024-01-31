
# Command-Line Argument Parsing with argparse

The `argparse` module is used for command-line argument parsing. In your script, `argparse.ArgumentParser` creates a parser object that will handle the command-line arguments. You've defined several arguments using `parser.add_argument()`. Here's how each of these arguments works and how to use them:

1. `--base-dir`: Specifies the base directory to scan. The default value is set to `BASE_DIR` from your configuration. Usage:

   ```sh
   python autoarch.py --base-dir "path/to/base/directory"
   ```
If you don't provide this argument, it will use the default value.

## --archive-dir: Specifies the directory where old projects will be archived. Default is ARCHIVE_DIR from your configuration. Usage:


python autoarch.py --archive-dir "path/to/archive/directory"
Omitting this argument will use the default.

--archive-after: Specifies the duration in seconds. Files older than this will be archived. Default is ARCHIVE_AFTER_SECONDS. Usage:


python autoarch.py --archive-after 86400  # Archives files older than 1 day
The default value is used if this argument is not provided.

--include-types: A list of file extensions to include in the archive. There's no default value. Usage:


python autoarch.py --include-types .txt .pdf .docx
This argument is optional.

--exclude-types: A list of file extensions to exclude from the archive. No default value. Usage:


python autoarch.py --exclude-types .mp3 .mp4 .avi
This is also optional.

### --exclude-dirs: A list of directories to exclude from the archive.

 ``No default value.`` 
 
## Usage:
```bash
python autoarch.py --exclude-dirs dir1 dir2 dir3
```
#### This is optional too.

- After defining the arguments, parser.parse_args() parses the arguments passed to the script. If you don't provide any arguments when running the script, the default values are used. If you provide arguments, they will override the defaults.

## You can combine these arguments as needed when running your script. For example:

``` bash
python autoarch.py --base-dir "/my/base/dir" --archive-dir "/my/archive/dir" --archive-after 604800 --include-types .txt .jpg --exclude-types .mp4 --exclude-dirs temp logs
```

