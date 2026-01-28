#function that calls itself
def sumOfNumbers(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + sumOfNumbers(n-1)

print("\n\nsumOfNumber: ")
print(sumOfNumbers(5))
