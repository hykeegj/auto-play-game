# LDPlayer ver 3.76 모바일 해상도 720 x 1280 320DPI 기준
import pyautogui as pag
import cv2
import sys
import time

# 안전모드 설정
pag.FAILSAFE = True

delay = 0.15
duration = 0
confidence = 0.5
gray_1 = cv2.IMREAD_GRAYSCALE

# 캐릭터가 왼쪽을 바라보고 있을 때 True, 오른쪽을 바라보고 있을 때 False (기본값 : True)
trigger_bool = True

# 게임 트리거 이미지 받아오기
up_button_img = cv2.imread('up_button.png', cv2.IMREAD_GRAYSCALE)  # 등산버튼
return_button_img = cv2.imread(
    'return_button.png', cv2.IMREAD_GRAYSCALE)  # 회전버튼
return_block_img = cv2.imread(
    'return_block.png', cv2.IMREAD_GRAYSCALE)  # 회전트리거
gameover1_img = cv2.imread('gameover1.png', cv2.IMREAD_GRAYSCALE)  # 게임오버1
gameover2_img = cv2.imread('gameover2.png', cv2.IMREAD_GRAYSCALE)  # 게임오버2

# 등산버튼 이미지 센터 좌표값 받아오기
up_button_center = pag.locateCenterOnScreen(
    up_button_img, grayscale=True, confidence=0.8)

# 회전버튼 이미지 센터 좌표값 받아오기
return_button_center = pag.locateCenterOnScreen(
    return_button_img, grayscale=True, confidence=0.8)

# 회전 트리거 이미지 영역 좌표값 계산하기
# 캐릭터가 왼쪽을 바라보고 있을 때
left_trigger_x = up_button_center.x - 365
left_trigger_y = up_button_center.y - 322

# 캐릭터가 오른쪽을 바라보고 있을 때
right_trigger_x = up_button_center.x - 147
right_trigger_y = up_button_center.y - 322

# 게임 시작시 무조건 첫 시작으로 등산버튼을 누름
print('스타트!, 등산!')
pag.click(up_button_center)
time.sleep(0.3)

while True:
    time.sleep(delay)
    set_left_trigger_1 = pag.locateOnScreen(return_block_img, region=(
        left_trigger_x, left_trigger_y, 75, 35), grayscale=True, confidence=confidence)
    set_left_trigger_2 = pag.locateOnScreen(return_block_img, region=(
        right_trigger_x, right_trigger_y, 75, 35), grayscale=True, confidence=confidence)

    print(trigger_bool)
    print(set_left_trigger_1)
    print(set_left_trigger_2)

    # 캐릭터가 왼쪽을 바라보고 있을 때, 트리거 이미지 위치에 블록 이미지가 없으면 회전버튼 클릭
    if trigger_bool == True and set_left_trigger_1 == None:
        print('왼쪽 바라보고 있는 캐릭터 회전!')
        pag.click(return_button_center)
        trigger_bool = False

    # 캐릭터가 오른쪽을 바라보고 있을 때, 트리거 이미지 위치에 블록 이미지가 없으면 회전버튼 클릭
    elif trigger_bool == False and set_left_trigger_2 == None:
        print('오른쪽 바라보고 있는 캐릭터 회전!')
        pag.click(return_button_center)
        trigger_bool = True

    # 왼쪽 또는 오른쪽 기준 트리거 이미지 위치에 블록 이미지가 있으면 등산버튼 클릭
    elif set_left_trigger_1 != None or set_left_trigger_2 != None:
        print('등산!')
        pag.click(up_button_center)

    # 게임오버시 캐릭터에 느낌표가 나타났을 때 프로그램 종료
