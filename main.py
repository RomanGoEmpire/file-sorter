import os
import logging

PATH = "Test_Vault"
DATA_PATH = f"{PATH}/Data"

IMAGE_PATH = f"{DATA_PATH}/Images"
VIDEO_PATH = f"{DATA_PATH}/Videos"


NEW_DATA_PATH = DATA_PATH + "/{folder}"
IMAGE_FORMATS = ["jpeg", "jpg", "png", "gif", "tiff", "bmp", "eps", "raw", "svg"]
VIDEO_FORMATS = [
    "mp4",
    "avi",
    "mov",
    "wmv",
    "flv",
    "mkv",
    "webm",
    "vob",
    "mts",
    "m4v",
    "3gp",
    "f4v",
]

logging.basicConfig(level=logging.DEBUG)


def get_files(path: str) -> list[str]:
    return [f for f in os.scandir(path) if f.is_file()]


def get_directories(path: str) -> list[str]:
    return [f.name for f in os.scandir(path) if f.is_dir()]


def create_folder(name: str) -> None:
    logging.info(f"Created Folder: {name}")
    os.makedirs(name=name, exist_ok=True)


def move_file(file: str, new_folder: str) -> None:
    logging.debug(f"Moved file to {new_folder}")
    os.rename(file, f"{new_folder}/{file.name}")


def main():
    create_folder(DATA_PATH)
    create_folder(IMAGE_PATH)

    files = get_files(PATH)
    directories = get_directories(DATA_PATH)

    for file in files:
        name, ending = file.name.split(".")

        if ending == ".md":
            continue

        if ending in IMAGE_FORMATS:
            new_folder = IMAGE_PATH
        elif ending in VIDEO_FORMATS:
            new_folder = VIDEO_PATH
        else:
            new_folder = NEW_DATA_PATH.format(folder=ending.upper())
            if new_folder not in directories:
                create_folder(new_folder)

        move_file(file, new_folder)


if __name__ == "__main__":
    main()
