'''The program takes in a number and finds the sum of digits in a number.'''
num=int(input("Enter the number = "))
tot=0
while(num>0):
    rem=num%10
    tot=tot+rem
    num=num//10
print("Sum of digit =",tot)
    
    
