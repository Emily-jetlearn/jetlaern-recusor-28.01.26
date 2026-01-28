def factorial(m):
    if m == 1 or m==0:
        return 1 
    else:
        return m*factorial(m-1)
    

num = int(input("enter a number: "))
print(f"factorial = {factorial(num)} ")