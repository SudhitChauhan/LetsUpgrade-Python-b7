list1 = []
for i in range(0,8):
	x=int(input("Add your list member : "))
	list1.append(x)
list2 = [1,1,5]
list3 = []
k = 0
j = 0
while (k<8):
	if (j==3):
		break
	joy=list2[j]
	if (list1[k]==joy):
		list3.append(list1[k])
		j = j + 1
		k = k + 1
	else:
		k=k+1
print("\n")
print(list1)
if (list3==list2):
	print("It's match !")
else:
	print("It's Gone !")
