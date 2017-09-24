class Account:
	def __init__(self,filepath):
		self.filepath = filepath
		with open(filepath,'r') as file:
			self.balance=int(file.read())
	def withdraw(self,amount):
		self.balance = self.balance - amount
	def deposit(self,amount):
		self.balance = self.balance +amount
	def commit(self):
		with open(self.filepath,'w') as file:
			file.write(self.balance)

class Checking(Account):
	"""Generate checking account objects makes use of Account to control balance"""
	type = "checking"
	def __init__(self,filepath fee):
		Account.__init__(self,filepath)
		self.fee = fee
	def transfer(self,amount):
		self.balance = self.balance -amount-self.fee

checking = Checking("balance.txt")
checking.transfer(10)
print(checking.balance)	
checking.commit()