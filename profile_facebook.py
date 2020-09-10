min_len = int(input("Minimum Dimension : "))
n = int (input("Total number of your photos : "))
for i in range(n):
	roy_width = int(input(" Your photo width : "))
	roy_high = int(input(" Your photo high : "))
	if ((roy_width<min_len) or (roy_high<min_len)):
		print("UPLOAD ANOTHER !")
	else:
		if (roy_width==roy_high):
			print("ACCEPTED !")
		else:
			print("CROP IT !")
	