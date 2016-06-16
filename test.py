def print_hello_world():
	print('hello world')

def other(n):
	if n <= 2:
		return 1
	else:
		return other(n-1) + other(n-2)

print_hello_world()
print(other(5))

print("This line is added by Alicia")