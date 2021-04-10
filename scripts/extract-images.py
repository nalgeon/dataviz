import os.path
from . import engine

BASE_PATH = "build"
SOURCE_PATH = os.path.join(BASE_PATH, "raw.html")
TARGET_PATH = os.path.join(BASE_PATH, "raw.images.html")


def main():
    file = open(SOURCE_PATH)
    source = file.read()
    file.close()

    target = engine.extract_images(source)
    file = open(TARGET_PATH, "w")
    file.write(target)
    file.close()


if __name__ == "__main__":
    main()