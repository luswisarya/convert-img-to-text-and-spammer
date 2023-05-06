#C:\Users\Asus\AppData\Local\Programs\Tesseract-OCR

import pyautogui
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Users\Asus\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = Image.open("image-to-convert.png")

output = pytesseract.image_to_string(img)
print(output)

#Use this instead to make the accuracy better
#img = Image.open("image-to-convert.png")
#new_size = tuple(4*x for x in img.size)
#img = img.resize(new_size, Image.ANTIALIAS)
#output = pytesseract.image_to_string(img)
