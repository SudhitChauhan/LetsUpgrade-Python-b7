String = str(input("Enter String : "))
x = 0
y = 0
u = len(String)
for i in range(u):
	if (String[i]=="L"):
		x = x - 1
	elif (String[i]=="R"):
		x = x + 1
	elif (String[i]=="U"):
		y = y + 1
	elif (String[i]=="D"):
		y = y - 1
	else :
		print("Not Satisfied String !")
print("Your String location :\n x : ",x,"\n y : ",y)