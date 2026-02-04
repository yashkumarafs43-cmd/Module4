#recursion is the process in which a function calls itself till a c
# certain condition is met
#without recursion

# def factorial(num1):
#     fact=1
#     while num1>1:
#         fact*=num1
#         num1-=1
#
#     return fact
#
# print(factorial(4))

#with recursion

def factorial(num):
    if num==1:   #Base Condition
        return 1
    else:
        fact=num*factorial(num-1)    #Recursion Condition
        return fact
n=int(input("Enter a number: "))
print(f'factorial of {n} is: {factorial(n)}')
