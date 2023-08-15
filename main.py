from PIL import Image


def main():
    im = Image.open("screenshot.jpg")
    im.show()


if __name__ == '__main__':
    main()
