"""
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 1

while True:
	if len(str(list(fib(n))[-1])) == 1000:
		print(n)
		exit()
	n += 1
