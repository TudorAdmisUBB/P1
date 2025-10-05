# This is a sample Python script.
from operator import truediv


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Hello")
def is_prime(number):
    if number<2:
        return False
    if number==2:
        return Truess0s0
    if number%2==0:
        return False
    for i in range (3,number-1,2):
        if number%i==0:
            return False
    return True
def FindPrimeNumber(n):
    if n<=2:
        return "Not possible"
    for i in range(n-1,1,-1):
        if is_prime(i):
            return i
    return "There are no prime numbers"
n=int(input("Enter a natural number: "))
print("The biggest prime number smaller then n is:")
result=FindPrimeNumber(n)
print(result)

