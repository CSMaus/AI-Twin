from PIL import Image
import pytesseract
import sys

# guide: https://www.linkedin.com/pulse/how-extract-text-from-image-using-python-yamil-garcia/
# tesseract: https://github.com/UB-Mannheim/tesseract/wiki

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img_path = 'details1_1_en.jpg'
img = Image.open(img_path)

text = pytesseract.image_to_string(img)
print(text)


# TODO: 1. Remake this to work as library. Make a Screen reader to work in background while game launched.
# TODO: 2. Need to run text parsing based on pressing certain key.
# TODO: 3. Parce text from certain area of the screen into different variables.
# TODO: 4. Filter parsed text: if parsed same parts of the text, when they follow each other - remove it from the second
# parsed
# TODO: 5. By pressing a key need to write parsed text into file with a name (name depends on key) and clear variable






