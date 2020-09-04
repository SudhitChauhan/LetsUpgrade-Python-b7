ft = int(input("Enter your current altitude :- "))
if (ft<=1000):
	print("Safe to land !")
elif (ft<=5000):
	print("Bring down to 1000")
else:
	print("Turn around")