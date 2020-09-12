def prime_number(num):

	if num>1:
		for i in range(2,num):
			if (num%i)==0:
				break
		else:
			print(num)

a=[]
for i in range(1,2500):
	a.append(i)

prime = filter(prime_number,a)
for num in prime:
	print(num)