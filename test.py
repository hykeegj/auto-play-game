import pyautogui as pag
import cv2
import time

# while True:
#     print(pag.position())
#     time.sleep(1)

up_button_img = cv2.imread('up_button.png', cv2.IMREAD_GRAYSCALE)
up_button_center = pag.locateCenterOnScreen(up_button_img, grayscale=True, confidence=0.9)
pag.moveTo(up_button_center)
print(up_button_center)

pag.moveTo(x=up_button_center.x - 365, y=up_button_center.y - 323, duration=0.5)
pag.moveTo(x=up_button_center.x - 227, y=up_button_center.y - 216, duration=0.5)

pag.moveTo(x=up_button_center.x - 147, y=up_button_center.y - 322, duration=0.5)
pag.moveTo(x=up_button_center.x - 64, y=up_button_center.y - 216, duration=0.5)

# 2120 1147
# 1755 824 / 1826 855
# 1973 825 / 2047 859