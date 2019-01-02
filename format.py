import os
import sys
from os import listdir
from os.path import isfile, join
from datetime import datetime, timezone


def format_files_in_directory(directory):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    markdowns = [f for f in onlyfiles if f[-2:] == 'md']
    for file in markdowns:
        filepath = os.path.join(directory, file)
        with open(filepath, 'r') as f:
            file_content = f.read()

        with open(filepath, 'w') as f:
            title = file[:-40].replace('-', ' ')
            date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
            front_matter = """---
layout: post
title:  "{}"
date:   {}
categories: jekyll update
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
