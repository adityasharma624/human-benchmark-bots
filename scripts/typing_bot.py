import pytesseract
import keyboard
from PIL import ImageGrab

region = (458, 359, 1440, 551)

while (not keyboard.is_pressed("s")):
    pass
screenshot = ImageGrab.grab(bbox=region)
text = pytesseract.image_to_string(screenshot)
text = text.replace("|", "I")
text = text.replace("\n", " ")

while (not keyboard.is_pressed("shift")):
    pass

keyboard.write(text)