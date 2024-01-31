import os
import shutil

def progress_bar(progress, total):
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    bar_width = terminal_width - 30

    percent = 100 * (progress / float(total))
    filled_length = int(bar_width * progress // total)

    bar_color = '\033[92m'
    reset_color = '\033[0m'

    bar = bar_color + '█' * filled_length + '-' * (bar_width - filled_length) + reset_color
    return f"[{bar}] {percent:.2f}%"

def should_include_file(file, include_types, exclude_types):
    if include_types:
        return any(file.endswith(ext) for ext in include_types)
    if exclude_types:
        return not any(file.endswith(ext) for ext in exclude_types)
    return True

def should_exclude_dir(dir, exclude_dirs):
    return any(ex_dir in dir for ex_dir in exclude_dirs)
