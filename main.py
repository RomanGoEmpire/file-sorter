import os
import re
import logging

os.chdir(os.path.expanduser("~/Documents/Central"))
PHOTOS_PATH = "Data/Videos"
files = sorted(os.listdir(PHOTOS_PATH))

for index, file in enumerate(files):
    base_files = [file.name for file in os.scandir(".") if file.is_file()]
    year = file[:4]
    year_md_file = f"Photos {year}.md"
    if year_md_file not in base_files:
        with open(year_md_file, "w") as f:
            f.write(
                """**Links:** [[Photos Album]]

"""
            )

    with open(year_md_file, "a") as f:
        f.write(
            f"""[[{file}]]
"""
        )
