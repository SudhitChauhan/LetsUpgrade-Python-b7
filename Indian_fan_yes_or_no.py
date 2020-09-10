import random
x = random.randrange(1,250)
for i in range(10):
	y = int(input("Guess India team Score : "))
	if (y<1) or (y>250):
		print("Reduce your expectation for 20-20 Cricket")
	elif (x==y):
		print("\nClose By, You are True Indian fan !")
		break
	else:
		print("Try again !\n")
		continue
else:
	print("You are not True Indian fan ! ")