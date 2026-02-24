# CB 1st Recursion Notes
for num in range(1,11):
    if num % 2 == 0:
        print(num)

even = []

num = 5

sum = 1

for x in range(1, num + 1):
    sum *= x

print(f"Loop: {sum}")

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(f"Recursion: {factorial(num)}")

fib = [1,1]

for i in range(1,11):
    fib.append(fib[i-1] + fib[i]) 

print("Loop: ")
for i in fib:
    print(i)

numbers = []

def fibonaci(n):
    
    if n == 2: 
        # numbers.append(n)
        return 1
    elif n == 1:
        return 0
    else:
        return fibonaci(n-1) + fibonaci(n-2)

print(f"Recursion: {fibonaci(10)}")