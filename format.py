import os
import sys
from os import listdir
from os.path import isfile, join
from datetime import datetime, timezone


POSTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '_posts')


def format_files_in_directory(directory):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    markdowns = [f for f in onlyfiles if f[-2:] == 'md']
    for file in markdowns:
        filepath = os.path.join(directory, file)
        with open(filepath, 'r') as f:
            file_content = f.read()

        date_today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        new_filepath = os.path.join(POSTS_DIR, date_today+'-'+file)
        with open(new_filepath, 'w') as f:
            title = file[:-40].replace('-', ' ')
            date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
            front_matter = """---
layout: post
title:  "{}"
date:   {}
---
""".format(title, date)
            file_content = front_matter + file_content
            f.write(file_content)


if __name__ == '__main__':
    export_name = sys.argv[1]
    export_dir = os.path.join(os.path.dirname(os.path.realpath(
        __file__)), 'exports', export_name)
    format_files_in_directory(export_dir)
    print('Formatted files in:', export_dir)
