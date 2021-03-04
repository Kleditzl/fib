def fib(input):
    try:
        input = int(input)
        if input < 0:
            return False
        if input == 1:
            return 0
        if input == 2 or input == 3:
            return 1
        else:
            return fib(input - 1)+ fib(input - 2)
    except ValueError:
        return False

def factorial(input):
    try:
        input = int(input)
        if input < 0:
            return False
        if input == 1 or input == 0:
            return 1
        else:
            fac = 1
            for i in range(1,input+ 1):
                fac = fac * i
            return fac
    except ValueError:
        return False
print(factorial(5))