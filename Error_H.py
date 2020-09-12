file = open("joy.txt",'w')
file.write("My name is Sudhit Chauhan , From Vadodara ,\nCurrently I am pursuing in BE in 7th-sem in IT(Infomation Technology) form SSECG at Bhavnager !")
file.close()
file = open("joy.txt",'r')
try:
	file.write("I like to play chess !")
except:
	print("unable to write in file !")
finally:
	file.close()