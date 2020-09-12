def armstrong(num):
	for x in range(1, num):
		if x>10:
			order = len(str(x))
			sum = 0 
			temp = x
			while temp > 0: 
				digit = temp % 10 
				sum += digit**order 
				temp //= 10
			if x == sum:
				yield print("T he First Armstrong Nubmer is : ", x) 
lst=list(armstrong(1000))