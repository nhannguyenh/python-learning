def factorial(num):
    if (type(num) != int) or (num < 0):
        return None
    else:
        sumOfFactorial = 1
        while num > 1:
            sumOfFactorial = sumOfFactorial * num
            num = num - 1
        return sumOfFactorial

print(factorial(5))