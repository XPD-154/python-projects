#fibonacci sequence is a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.

def fib(n):
    a = 0
    b = 1

    if n <= 0:
        fib(int(input('Enter a positive number other than 0: ')))
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fib(int(input("enter a maximum for the range of fibonnaci sequence: ")))
