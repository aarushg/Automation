import pyautogui, time

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'tell bob i said hi.'}]
nameField = (210,527)
submitButton = (154, 324)
submitButtonColor = (75, 141, 249)

for person in formData:
	print('>>> 3 second pause to press crl c<<<')
	time.sleep(3)

	#while not pyautogui.pixelMatchesColor(submitButton[0],submitButton[1],submitButtonColor):
		#time.sleep(0.5)
	print('Entering %s info' %(person['name']))
	pyautogui.click(nameField[0], nameField[1])
	pyautogui.typewrite(' ' + '\t', 0.25)
	pyautogui.typewrite(person['name'] + '\t',.10)
	pyautogui.typewrite(person['fear'] + '\t',.10)

	if person['source'] == 'wand':
		pyautogui.typewrite('down'+ '\t', 0.25)
		#pyautogui.press('enter')
		#pyautogui.typewrite(['\t'])
	elif person['source'] == 'amulet':
		pyautogui.typewrite(['down','down','enter', '\t'])
	elif person['source'] == 'crystal ball':
		pyautogui.typewrite(['down','down','down','enter', '\t'])
	elif person['source'] == 'money':
		pyautogui.typewrite(['down','down','down','down','enter', '\t'])


	if person['robocop'] == 1:
		pyauto.typewriter([' ', '\t'])
	elif person['robocop'] == 2:
		pyautogui.typewrite(['right', '\t'])
	elif person['robocop'] == 3:
		pyautogui.typewrite(['right','right', '\t'])
	elif person['robocop'] == 4:
		pyautogui.typewrite(['right','right','right', '\t'])
	elif person['robocop'] == 5:
		pyautogui.typewrite(['right','right','right','right','\t'])

	pyautogui.typewrite(person['comments'] +'\t')
	pyautogui.press('enter')
	#pyautogui.click(651, 817)

