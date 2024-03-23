from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"
outPath = "/editedImgs"


def editPhoto(path, outPath):
  for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert("L")

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    cleanName = os.path.splitext(filename)[0]

    edit.save(f".{outPath}/{cleanName}_edited.jpg")

if __name__ == "__main__":
  editPhoto(path, outPath)