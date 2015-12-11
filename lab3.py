#Matt Layman CS113 lab3.py
class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return (self.items == [])

def eval_postfix(expr):
	import re
	token_list = re.split("([^0-9])", expr)
	stack = Stack()
	for token in token_list:
		if token == "" or token == " ":
			continue
		if token == "+":
			sum = stack.pop() + stack.pop()
			stack.push(sum)
		elif token == "*":
			product = stack.pop() * stack.pop()
			stack.push(product)
		else:
			stack.push(int(token))
	return stack.pop()

if __name__ == "__main__":
	"""
	s = Stack()
	s.push(54)
	s.push(45)
	s.push("+")

	while not s.is_empty():
		print(s.pop(), end=" ")"""

	print(eval_postfix("1 2 + 3 *"))
	print(eval_postfix("3 2 * 1 +"))
