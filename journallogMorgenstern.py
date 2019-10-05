title="Aiko Morgenstern\'s Journal Log"
print(title)
date="7th february 3016, Gregorian Calendar"
dateday=7
datemonth=2
dateyear=3016
if dateday+datemonth+dateyear>6000:
	print(date)
	#comments about the weather
	weather="cloudy"
	if weather=="outerspace":
		print ("Damn! still stuck in outer space!")
		
	elif weather=="moist":
		print ("Moisture! Water is good!")
else:
	print ("Wow! This planetary atmosphere looks interesting!")
	if 2<3:
		print("Blue")

#datecommands		
def date2(date, dateday, datemonth, dateyear):
	
	if dateday+datemonth+dateyear>2000:
		print ("It\'s", date, "today.")
date2("gzg", 9, 68, 3453)
date2("flowers", 1359, 9789668, 3453)
date2(date, dateday, datemonth, dateyear)

def hi():
	print('Hi there!')
	print('How are you?')
hi()

#variables for dressing up aiko in the morning
aikosclothes = ["skirt", "yellow bouse", "mouthrat", "floral print dress", "spacesuit"]
print (aikosclothes)



