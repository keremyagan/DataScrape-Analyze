from PIL import Image
from pytesseract import pytesseract
import requests
import os
class ImagetoText():
    def __init__(self,url,lang="tur"):
        self.url=url
        self.lang=lang
        self.path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        
    def text(self):
        try:
            with open('pic1.jpg', 'wb') as handle:
                response = requests.get(self.url, stream=True)
                if not response.ok:
                    print (response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
            image_path = "pic1.jpg"
            img = Image.open(image_path)
            pytesseract.tesseract_cmd = self.path_to_tesseract
            text = pytesseract.image_to_string(img,lang=self.lang)
            os.remove("pic1.jpg")
            return text[:-1]
        except Exception as err:
            return f"An Error Occured:{err} "

    def download(self):
        """
        Just downloads the image
        """
        try:
            with open('pic1.jpg', 'wb') as handle:
                response = requests.get(self.url, stream=True)
                if not response.ok:
                    print (response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)

            image_path = "pic1.jpg"
            img = Image.open(image_path)
            pytesseract.tesseract_cmd = self.path_to_tesseract
            text = pytesseract.image_to_string(img,lang=self.lang)
            return "Image Saved to pic1.jpg"
        except Exception as err:
            return f"An Error Occured:{err} "