import pyautogui as pag
import cv2
import numpy as np

up_button_img = cv2.imread('up_button.png')
print(pag.locateOnScreen(up_button_img))
