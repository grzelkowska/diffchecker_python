import cv2
import os, time
import pyautogui
from PIL import ImageChops


# time.sleep(3)

while True:

    result = pyautogui.confirm("diffChecker", buttons=["start", "end"])
    if result == "end":
        break

    time.sleep(1)

    width = 894 - 296
    height = 808 - 310
    y_pos = 310

    src = pyautogui.screenshot(region=(296 * 2, 310 * 2, 2 * width, 2 * height))
    # src_jpg = src.convert("RGB")
    # src_jpg.save("src.jpg")
    dest = pyautogui.screenshot(region=(907 * 2, 310 * 2, width * 2, height * 2))
    # dest_jpg = dest.convert("RGB")
    # dest_jpg.save("dest.jpg")

    diff = ImageChops.difference(src, dest)
    diff_jpg = diff.convert("RGB")
    diff_jpg.save("diff.jpg")

    while not os.path.exists("diff.jpg"):
        time.sleep(1)

    diff_img = cv2.imread("diff.jpg")

    gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    COLOR = (0, 200, 0)

    for cnt in contours:
        if cv2.contourArea(cnt) > 300:  #
            x, y, width, height = cv2.boundingRect(cnt)
            # cv2.rectangle(src_img, (x, y), (x + width, y + height), COLOR, 2)
            # cv2.rectangle(dest_img, (x, y), (x + width, y + height), COLOR, 2)
            cv2.rectangle(diff_img, (x, y), (x + width, y + height), COLOR, 2)

            to_x = (x + (width // 2)) // 2 + 296
            to_y = (y + (height // 2)) // 2 + y_pos
            pyautogui.moveTo(to_x, to_y, duration=0.5)
            pyautogui.click()

    cv2.imshow("diff", diff_img)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
