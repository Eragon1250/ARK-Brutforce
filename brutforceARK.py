from pynput.keyboard import Key, Controller
import keyboard as key
import time
a = 0
keyboard = Controller()
list=[0,1,2,3,4,5,6,7,8,9]
time.sleep(5)
while not key.is_pressed('ß'):

	print("Die ß Taste wird gerade nicht gedrückt")

	for i in list:
		for j in list:
			for k in list:
				for l in list:
					keyboard.press(str(i))
					keyboard.release(str(i))
					keyboard.press(str(j))
					keyboard.release(str(j))
					keyboard.press(str(k))
					keyboard.release(str(k))
					keyboard.press(str(l))
					keyboard.release(str(l))
					time.sleep(0.7)
					keyboard.press('e')
					time.sleep(0.2)
					keyboard.release('e')
					time.sleep(0.5)
					time.sleep(0.000001)


# 0 = (892, 728)
# 1 = (891, 524)
# 2 = (961, 522)
# 3 = (1027, 523)
# 4 = (885, 592)
# 5 = (960, 596)
# 6 = (1031, 589)
# 7 = (892, 663)
# 8 = (959, 661)
# 9 = (1027, 658)