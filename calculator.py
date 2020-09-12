def sum(x,y):
	print("Your two number addition is ",x+y)
def mul(x,y):
	print("Your two number multiplication is ",x*y)
def sub(x,y):
	print("Your two numner subtraction is ",x-y)
def div(x,y):
	if(y!=0):
		print("Your two number divition is ",x/y)
	else:
		print("Imposible")
x = int(input("Enter your first number : "))
y = int(input("Enter your second number : "))
print("\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n")
z = int(input("Enter your opration number :  "))
if(z==1):
	sum(x,y)
elif(z==2):
	sub(x,y)
elif(z==3):
	mul(x,y)
elif(z==4):
	div(x,y)
else:
	print("Unvalied Number !")
	