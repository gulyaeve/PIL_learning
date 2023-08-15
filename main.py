from PIL import Image

im = Image.open("screenshot.jpg")


def main():
    print(im.format, im.size, im.mode)

    size = (128, 128)
    outfile = "screenshot_thumbnail.png"

    im.thumbnail(size)
    im.save(outfile, "PNG")

    newfile = Image.open(outfile)
    print(newfile.format, newfile.size, newfile.mode)


def crop_image():
    box = (100, 100, 400, 400)
    region = im.crop(box)
    region.save("screenshot_cropped.jpg", "JPEG")


if __name__ == '__main__':
    crop_image()
