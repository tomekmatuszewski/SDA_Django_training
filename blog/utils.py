from PIL import Image

def change_pic_size(path, height, width) -> None:
    img = Image.open(path)
    if img.height > height or img.width > width:
        output_size = (width, height)
        img.thumbnail(output_size)
        img.save(path)




