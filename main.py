from PIL import Image


def main():
    im = Image.open("screenshot.jpg")
    print(im.format, im.size, im.mode)

    size = (128, 128)
    outfile = "screenshot_thumbnail.png"

    im.thumbnail(size)
    im.save(outfile, "PNG")

    newfile = Image.open(outfile)
    print(newfile.format, newfile.size, newfile.mode)


if __name__ == '__main__':
    main()
