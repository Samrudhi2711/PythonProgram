'''Write a Python Program to check whether a given number is a palindrome.'''
num=int(input("Enter the number"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=(rev*10)+dig
    num=num//10
print("Reverse no. =",rev)
if(temp==rev):
    print("Entered number is palindrome",temp)
else:
    print("Entered Number is not palindrome",temp)
