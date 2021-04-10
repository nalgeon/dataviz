import os.path
import markdownify

BASE_PATH = "build"
SOURCE_PATH = os.path.join(BASE_PATH, "raw.extract.html")
TARGET_PATH = os.path.join(BASE_PATH, "raw.md")


def main():
    file = open(SOURCE_PATH)
    source = file.read()
    file.close()

    target = markdownify.markdownify(source)
    file = open(TARGET_PATH, "w")
    file.write(target)
    file.close()


if __name__ == "__main__":
    main()