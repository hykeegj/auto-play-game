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

pag.moveTo(x=up_button_center.x - 278, y=up_button_center.y - 241, duration=0.5)
pag.moveTo(x=up_button_center.x - 227, y=up_button_center.y - 216, duration=0.5)

pag.moveTo(x=up_button_center.x - 111, y=up_button_center.y - 240, duration=0.5)
pag.moveTo(x=up_button_center.x - 64, y=up_button_center.y - 216, duration=0.5)

# 2023 1068
# 1912 828
# 1959 852