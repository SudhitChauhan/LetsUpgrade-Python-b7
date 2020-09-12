class bank_account:
	def __init__(self):
		self.balance = 0
		print("Your new account created !")
	def deposit(self):
		amount = int(input("Enter the amount to deposit : "))
		self.balance+=amount
		print("Successful !")
	def withdraw(self):
		amount = int(input("Enter the amount to withdraw : "))
		if amount>self.balance:
			print("Insufficient balance !")
		else:
			self.balance-=amount
		print("\nSuccessful !")
		print("Your remaining balance ",self.balance)

x = bank_account()
x.deposit()
x.withdraw()