arr = []
def getInput(calculate_arg_fun):
	def wrap_function():
		b = int(input("Enter upper limit :  ")) 
		a = int(input("Enter lower limit : ")) 
		for i in range(a,b):
			calculate_arg_fun(i)
	return wrap_function 
@getInput
def prime(num):
	check = 0
	for y in range(2, num):
		if num%y == 0:
			check+=1 
	if check==0 and num != 1:
		arr.append(num)
prime()
print(arr)