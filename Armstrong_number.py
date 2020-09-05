for a in range(1042000,702648265):
	mul=len(str(a))
	sum=0
	num=a
	while(num>0):
		dig=num%10
		sum=sum+(dig**mul)
		num=num//10
	if(sum==a):
		print("The first ArmStrong number is : .........",a)
		break