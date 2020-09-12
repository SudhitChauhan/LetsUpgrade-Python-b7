def fibonacci_series(num):
	print(num)
	result = num
	for i in range(10):
		x = result + num
		print(x)
		num = result
		result = x 

		
num = int(input("Enter your strating number : "))
fibonacci_series(num)	
		