def print_hello_world():
	print('hello world')

def other(n):
	if n > 0:
		return other(n-1)+1
	else:
		return(1)

print_hello_world()
print(other(5))