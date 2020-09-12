import random
Thriller = ["The Perfection","A Quiet Place","The Body","Extraction","Joker","Don't Breathe"]
RomCom = ["Kapoor & Sons","Befikre","Tall Girl","The Perfect Date","Meri Pyaari Bindu","The Spectacular Now"]
Action = ["Bloodshot","Venom","San Andreas","Wonder Woman","Suicide Squad","Alita: Battle Angel"]
Anime = ["Akira","Whisper of the Heart","A Whisker Away","A Silent Voice","Batman Ninja","My Neighbor Totoro"]
print("Anime\nAction\nRomCom\nThriller")
x = input("What kind of movies do you want to watch?\n")
if x=='Anime':
	print(random.choice(Anime))
	print(random.choice(Anime))
elif x=='Action':
	print(random.choice(Action))
	print(random.choice(Action))
elif x=='RomCom':
	print(random.choice(RomCom))
	print(random.choice(RomCom))
elif x=='Thriller':
	print(random.choice(Thriller))
	print(random.choice(Thriller))
else:
	print("Enter Valied Type !")
	