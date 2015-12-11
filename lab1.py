#Matt Layman CS113 lab1.py
class Accounts:
	def __init__(self, firstname, lastname, intdeposit):
		self.firstname = firstname
		self.lastname = lastname
		self.balance = intdeposit

	def deposit(self, amount):
		#returns balance after depositing amount
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		#returns balance after withdrawing amount
		if amount > self.balance:
			raise RuntimeError("Amount greater than available balance.")
		self.balance -= amount
		return self.balance

	def fee_calculations(self):
		#if balance < 1000, subtract $10 fee
		if self.balance < 1000:
			self.balance -= 10
		return self.balance

	def interest(self, interest=.03):
		#add 3% interest to balance
		self.balance += self.balance*(interest/12)
		return self.balance


if __name__ == "__main__":
	myact = Accounts('Matt', 'Layman', 900)
	print(myact.firstname, myact.lastname, myact.balance, myact.deposit(10), myact.withdraw(100), myact.fee_calculations(), myact.interest())
