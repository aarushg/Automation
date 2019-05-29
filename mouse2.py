import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

try:
	while True:
		x,y = pyautogui.position()
		positionStr = 'X: ' + str(x).rjust(4) + 'Y: '+ str(y).rjust(4)
		pixelColor = pyautogui.screenshot().getpixel((x,y))
		positionStr +=' RGB: (' + str(pixelColor[0]).rjust(3) + ', ' + str(pixelColor[1]).rjust(3) + ', ' + str(pixelColor[2]).rjust(3) +')'	
		print(positionStr, end=' ')

except KeyboardInterrupt:
	print('\nDone')
