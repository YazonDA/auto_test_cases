import pyautogui
from time import sleep


size_x, size_y = pyautogui.size() # 1920, 1080

# pos_x, pos_y = 1910, 15
factor_x, factor_y = 0.994791666666667, 0.013888888888889
pyautogui.click(x=size_x*factor_x, y=size_y*factor_y)
sleep(1)

# pos_x, pos_y = 1750, 165
factor_x, factor_y = 0.911458333333333, 0.152777777777778
pyautogui.click(x=size_x*factor_x, y=size_y*factor_y)
