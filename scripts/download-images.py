import os.path
from . import engine

BASE_PATH = "build"
SOURCE_PATH = os.path.join(BASE_PATH, "raw.images.html")
TARGET_PATH = os.path.join(BASE_PATH, "img")


def main():
    file = open(SOURCE_PATH)
    source = file.read()
    file.close()
    engine.download_images(source, to=TARGET_PATH)


if __name__ == "__main__":
    main()