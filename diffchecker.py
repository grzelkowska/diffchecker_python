import pyautogui
from PIL import ImageChops

import time

time.sleep(3)

# left image, right image
# (55, 73). (901, 73)
# width: 899 - 55 = 843
# height: 1146 - 73 = 1073
width, height = 844, 1073
y_pos = 73

src = pyautogui.screenshot(region=(55 * 2, 73 * 2, 2 * width, 2 * height))
src.save("src.png")

dest = pyautogui.screenshot(region=(901 * 2, 73 * 2, width * 2, height * 2))
dest.save("dest.png")
