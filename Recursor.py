#function that calls itself
def sumOfNumbers(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + sumOfNumbers()

print("\n\nsumOfNumber: ")
print(sumOfNumbers(5))
